from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.contrib.auth import login, logout, authenticate
from django.urls import resolve, reverse
from .forms import LoginForm, RegisterForm, BookForm, MovieForm, MusicForm, \
    MagazineForm, ItemSelectorForm, ItemSortingForm, BookFilterForm, MagazineFilterForm, \
    MusicFilterForm, MovieFilterForm, LoanHistoryFilterForm
from .gateways import add_user, get_all_users, get_all_items, \
    get_magazines, get_movies, get_musics, get_books, insert_item, unique_email, \
    edit_items, get_book, get_movie, get_magazine, get_music, delete_item, update_cart, \
    get_cart, expand_item, new_loan, get_unloaned, get_active_loans, get_quantity_available, \
    return_item, get_all_loans, get_all_loaned_item_instances, get_quantity

from .auth import authorize_admin, authorize_client
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime

MAX_LOANS = 20

def index(request):
    response = render(request, 'biblioteca/index.html')
    print(request.COOKIES)
    if('sessionid' in request.COOKIES):
        response.set_cookie('sessionid', request.COOKIES['sessionid'])
    print(request.user.is_authenticated)
    print(request.session.session_key)
    return response

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("=========USER==========")
                print(user.email)
                # user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                request.session.modified = True
                request.session.save()
                print(request.user.is_authenticated)
                print(request.session.session_key)
                if request.user.role_id==1:
                    return HttpResponseRedirect('admin')
                else:
                    return HttpResponseRedirect('client')
            else:
                return redirect('login')
    else:
        if request.user.is_authenticated:
            if(int(request.user.role_id == 1)):
                return HttpResponseRedirect('admin')
            else:
                return HttpResponseRedirect('client')
        print(request.user.is_authenticated)
        print(request.session.session_key)
        form = LoginForm()
        return render(request, 'biblioteca/login.html', {'form': form})

def end_session(request):
    logout(request)
    return HttpResponseRedirect('/')

# Client stuff

def client_landing(request):
    if not authorize_client(request):
        return HttpResponseRedirect(reverse('admin_landing'))
    return render(request, 'biblioteca/client/landing.html')

def view_cart(request):
    if not authorize_client(request):
        return HttpResponseRedirect(reverse('admin_landing'))
    cart = get_cart(request.user.id)
    expanded_cart = []
    for item in cart:
        new_item = expand_item(item)
        print(new_item)
        if new_item is None: 
            delete_from_cart(request, item)
            return render(request, 'biblioteca/client/cart.html', {'cart': expanded_cart, 'messages': ['One or more items in your cart have been deleted.']})
        new_item['item_type'] = new_item['item_type'].capitalize()
        expanded_cart.append(new_item)
    print(expanded_cart)
    error = []
    if 'quantity' in request.GET:
        error.append("One or more of your items is not in stock. Please check quantity available on the catalog page")
    return render(request, 'biblioteca/client/cart.html', {'cart': expanded_cart, 'error': error})

@csrf_exempt
def add_to_cart(request):
    if not authorize_client(request):
        pass
    if request.method == 'POST':
        current_cart = get_cart(request.user.id)
        current_cart.append(request.POST.get('id'))
        item_type = update_cart(request.user.id, current_cart, new_id=request.POST.get('id'))
        return HttpResponseRedirect(('/client/items' + '?item_type=' + item_type))

@csrf_exempt
def delete_from_cart(request, item_id = None):
    if not authorize_client(request):
        pass
    if request.method == 'POST':
        current_cart = get_cart(request.user.id)
        item_to_remove = request.POST.get('id')
        current_cart.remove(item_to_remove)
        update_cart(request.user.id, current_cart)
    else:
        current_cart = get_cart(request.user.id)
        item_to_remove = item_id
        current_cart.remove(item_to_remove)
        update_cart(request.user.id, current_cart)
    return HttpResponseRedirect('/client/cart')

def get_loans(request):
    if not authorize_client(request):
        return HttpResponseRedirect(reverse('admin_landing'))
    loans = get_active_loans(request.user.id)
    expanded_loans = []
    for loan in loans:
        item_id = loan['stock_id'].split('-')[0]
        expanded_item = expand_item(item_id)
        expanded_item['loan_id'] = loan['id']
        expanded_item['lent_date'] = loan['lent_date']
        expanded_item['return_date'] = loan['return_date']
        if (loan['return_date'] < datetime.now()) and (int(loan['state_id']) == 1):
            expanded_item['loan_status'] = 'Late'
        else:
            expanded_item['loan_status'] = 'Active'
        expanded_item['item_type'] = expanded_item['item_type'].capitalize()
        expanded_loans.append(expanded_item)
    loansCart = get_cart(request.user.id)
    return render(request, 'biblioteca/client/view_loans.html', {'loans' : expanded_loans, 'cart' : loansCart})

@csrf_exempt
def return_loan(request):
    if not authorize_client(request):
        pass
    if request.method == 'POST':
        return_item(request.POST.get('id'))
        return HttpResponseRedirect('/client/view_loans')

@csrf_exempt
def checkout(request):
    if not authorize_client(request):
        pass
    if len(get_active_loans(request.user.id)) > 20:
        return render(request,'/client/cart')
    cart = get_cart(request.user.id)
    # check quantity
    simplified_cart = _cart_to_quantities(cart)
    try:
        for key, value in simplified_cart.items():
            if get_quantity_available(key) < value:
                return HttpResponseRedirect('/client/cart?quantity=invalid')
    except:
        return HttpResponseRedirect('/client/cart')
    # check if exceeds max loans:
    total_loans = len(get_active_loans(request.user.id)) + len(cart)
    if total_loans > MAX_LOANS:
        return HttpResponseRedirect('/client/cart')
    for item in cart:
        stock_id = get_unloaned(item)
        print(request.user.id)
        print(expand_item(item)['item_type'])
        new_loan(request.user.id, stock_id, expand_item(item)['item_type'])
    return HttpResponseRedirect('/client')

def _cart_to_quantities(cart):
    simplified_cart = {}
    for item in cart:
        if item not in simplified_cart:
            simplified_cart[item] = 1
        else:
            simplified_cart[item] = simplified_cart[item] + 1
    return simplified_cart

# Admin Stuff

def admin_landing(request):
    if not authorize_admin(request):
        raise PermissionDenied
    return render(request, 'biblioteca/admin/landing.html')  

def register_user(request):
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        error_list = list()
        user_details = dict()
        user_details['email'] = request.POST.get('email')
        if unique_email(user_details['email']) == False: 
            error_list.append('This e-mail already exists.')
            return render(request, 'biblioteca/admin/register_users.html', {'form' : form, 'error_list' : error_list})
        if form.is_valid():
            user_details['password'] = request.POST.get('password')
            user_details['f_name'] = request.POST.get('f_name')
            user_details['l_name'] = request.POST.get('l_name')
            user_details['address'] = request.POST.get('address')
            user_details['phone_num'] = request.POST.get('phone_num')
            if 'isAdmin' in request.POST:
                user_details['role_id'] = '1'
            else:
                user_details['role_id'] = '2'
            add_user(user_details)
            return HttpResponseRedirect('/admin/register')
        else:
            for error in form.errors:
                error_list.append(form[error].label + " is invalid.")
            return render(request, 'biblioteca/admin/register_users.html', {'form' : form, 'error_list' : error_list})    
    else:	
        form = RegisterForm
        error = ''
        return render(request, 'biblioteca/admin/register_users.html', {'form': form, 'error': error})

def add_item(request, item_type = None):
    item_details = dict()
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        if item_type == 'Book':
            form = BookForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['author'] = request.POST.get('author')
            item_details['format'] = request.POST.get('format')
            item_details['pages'] = request.POST.get('pages')
            item_details['publisher'] = request.POST.get('publisher')
            item_details['language'] = request.POST.get('language')
            item_details['isbn_10'] = request.POST.get('isbn_10')
            item_details['isbn_13'] = request.POST.get('isbn_13')
            item_details['quantity'] = request.POST.get('quantity')
        elif item_type == 'Movie':
            form = MovieForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['director'] = request.POST.get('director')
            item_details['producers'] = request.POST.get('producers')
            item_details['actors'] = request.POST.get('actors')
            item_details['language'] = request.POST.get('language')
            item_details['subtitles'] = request.POST.get('subtitles')
            item_details['dubbed'] = request.POST.get('dubbed')
            item_details['release_date'] = request.POST.get('release_date')
            item_details['run_time'] = request.POST.get('run_time')
            item_details['quantity'] = request.POST.get('quantity')
        elif item_type == 'Music':
            form = MusicForm(request.POST)
            item_details['type'] = request.POST.get('type')
            item_details['title'] = request.POST.get('title')
            item_details['artist'] = request.POST.get('artist')
            item_details['label'] = request.POST.get('label')
            item_details['release_date'] = request.POST.get('release_date')
            item_details['asin'] = request.POST.get('asin')
            item_details['quantity'] = request.POST.get('quantity')
        elif item_type == 'Magazine':
            form = MagazineForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['publisher'] = request.POST.get('publisher')
            item_details['language'] = request.POST.get('language')
            item_details['isbn_10'] = request.POST.get('isbn_10')
            item_details['isbn_13'] = request.POST.get('isbn_13')
            item_details['quantity'] = request.POST.get('quantity')
        if form.is_valid():
            for key in item_details:
                item_details[key].lstrip("0")
            insert_item(item_details, item_type)
            messages.success(request, "Item added successfully!")
            return HttpResponseRedirect('/admin/add_item/' + item_type) 
        else:
            for error in form.errors:
                messages.error(request, form[error].label + " is invalid.")
            return render(request, 'biblioteca/admin/add_item.html', {'form' : form, 'item_type' : item_type})
    else:
        if item_type == 'Book':
            form = BookForm
            return render(request, 'biblioteca/admin/add_item.html', {'form': form, 'item_type': 'Book'})
        elif item_type == 'Movie':
            form = MovieForm
            return render(request, 'biblioteca/admin/add_item.html', {'form': form, 'item_type': 'Movie'})
        elif item_type == 'Magazine':
            form = MagazineForm
            return render(request, 'biblioteca/admin/add_item.html', {'form': form, 'item_type': 'Magazine'})
        elif item_type == 'Music':
            form = MusicForm
            return render(request, 'biblioteca/admin/add_item.html', {'form': form, 'item_type': 'Music'})

@csrf_exempt
def item_delete(request):
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        id = request.POST.get('id')
        item_type = request.POST.get('item_type')
        get_string = ""
        if item_type == 'Book':
            get_string = "?item_type=Book"
        elif item_type == 'Movie':
            get_string = "?item_type=Movie"
        elif item_type == 'Music':
            get_string = "?item_type=Music"
        elif item_type == "Magazine":
            get_string = "?item_type=Magazine"
        loaned_items = get_all_loaned_item_instances(id)
        if len(loaned_items) != 0:
            return HttpResponseRedirect('/admin/items' + get_string)
        delete_item(id)
        return HttpResponseRedirect('/admin/items' + get_string)

def get_users(request):
    if not authorize_admin(request):
        raise PermissionDenied
    users = get_all_users()
    print(users)
    return render(request, 'biblioteca/admin/view_users.html', {'users': users})

@csrf_exempt
def get_items(request):
    current_url = resolve(request.path_info).url_name
    print(current_url)
    if current_url.startswith('admin_view_items'):
        if not authorize_admin(request) and not authorize_client(request):
            raise PermissionDenied
        elif not authorize_admin(request) and authorize_client(request):
            return HttpResponseRedirect(reverse('client_view_items'))
    if current_url.startswith('client_view_items'):
        if not authorize_client(request) and not authorize_admin(request):
            raise PermissionDenied
        elif not authorize_client(request) and authorize_admin(request):
            return HttpResponseRedirect(reverse('admin_view_items'))    
    item_type = request.GET.get('item_type')
    form = ItemSelectorForm()
    print(item_type)
    if item_type == "Book":
        items = get_books()
        form.initial = {"item_type": "Book"}
        languages = set()
        publishers = set()
        formats = set()
        for book in items:
            languages.add(book['language'])
            publishers.add(book['publisher'])
            formats.add(book['format'])
        languages = sorted(languages)
        publishers = sorted(publishers)
        formats = sorted(formats)
        filter_form = BookFilterForm(languages, publishers, formats)
        filter_form.initial = {'language_filter': request.GET.get('language_filter'),
                               'publisher_filter': request.GET.get('publisher_filter'),
                               'format_filter': request.GET.get('format_filter')}
    elif item_type == "Music":
        items = get_musics()
        form.initial = {"item_type": "Music"}
        types = set()
        labels = set()
        artists = set()
        for music in items:
            types.add(music['type'])
            labels.add(music['label'])
            artists.add(music['artist'])
        types = sorted(types)
        labels = sorted(labels)
        artists = sorted(artists)
        filter_form = MusicFilterForm(types, labels, artists)
        filter_form.initial = {'type_filter': request.GET.get('type_filter'),
                               'label_filter': request.GET.get('label_filter'),
                               'artist_filter': request.GET.get('artist_filter')}
    elif item_type == "Movie":
        items = get_movies()
        form.initial = {"item_type": "Movie"}
        directors = set()
        languages = set()
        for movie in items:
            directors.add(movie['director'])
            languages.add(movie['language'])
        directors = sorted(directors)
        languages = sorted(languages)
        filter_form = MovieFilterForm(directors, languages)
        filter_form.initial = {'director_filter': request.GET.get('director_filter'),
                               'language_filter': request.GET.get('language_filter')}
    else:
        # Defaults to magazine.
        item_type = "Magazine"
        items = get_magazines()
        form.initial = {"item_type": "Magazine"}
        languages = set()
        publishers = set()
        for magazine in items:
            languages.add(magazine['language'])
            publishers.add(magazine['publisher'])
        languages = sorted(languages)
        publishers = sorted(publishers)
        filter_form = MagazineFilterForm(languages, publishers)
        filter_form.initial = {'language_filter': request.GET.get('language_filter'),
                               'publisher_filter': request.GET.get('publisher_filter')}
    print(items)

    if request.GET.get("apply_filter") or request.GET.get("change_sorting_type"):
        if item_type == 'Magazine':
            items = filtered_magazine(items, request)
        elif item_type == 'Book':
            items = filtered_book(items, request)
        elif item_type == 'Movie':
            items = filtered_movie(items, request)
        elif item_type == 'Music':
            items = filtered_music(items, request)

    sorting_options = []
    if len(items) != 0:
        for key in items[0]:
            sorting_options.append(key)
    print(sorting_options)
    sorting_form = ItemSortingForm(sorting_options)
    if not request.GET.get("change_sorting_type"):
        sorting_type = 'id'
    else:
        sorting_type = request.GET.get('sort_by')
    sorting_form.initial = {'sort_by': sorting_type}

    if sorting_type is not None:
        items = sorted(items, key=lambda k: k[sorting_type])

    if current_url.startswith('admin_view_items'):
        return render(request, 'biblioteca/admin/view_items.html', {'items': items, 'form': form,
                                                                    'sorting_form': sorting_form,
                                                                    'filter_form': filter_form})
    elif current_url.startswith('client_view_items'):
        cart = get_cart(request.user.id)
        return render(request, 'biblioteca/client/view_items.html', {'items': items, 'form': form,
                                                                     'sorting_form': sorting_form,
                                                                     'filter_form': filter_form,
                                                                     'cart': cart, 'item_type': item_type})

def edit_item(request, item_type=None, item_id=None):
    item_details = dict()
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        quantity_valid = True
        get_string = ""
        if item_type == 'Book':
            form = BookForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['author'] = request.POST.get('author')
            item_details['format'] = request.POST.get('format')
            item_details['pages'] = request.POST.get('pages')
            item_details['publisher'] = request.POST.get('publisher')
            item_details['language'] = request.POST.get('language')
            item_details['isbn_10'] = request.POST.get('isbn_10')
            item_details['isbn_13'] = request.POST.get('isbn_13')
            item_details['quantity'] = request.POST.get('quantity')
            get_string = "?item_type=Book"
        elif item_type == 'Movie':
            form = MovieForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['director'] = request.POST.get('director')
            item_details['producers'] = request.POST.get('producers')
            item_details['actors'] = request.POST.get('actors')
            item_details['language'] = request.POST.get('language')
            item_details['subtitles'] = request.POST.get('subtitles')
            item_details['dubbed'] = request.POST.get('dubbed')
            item_details['release_date'] = request.POST.get('release_date')
            item_details['run_time'] = request.POST.get('run_time')
            item_details['quantity'] = request.POST.get('quantity')
        elif item_type == 'Music':
            form = MusicForm(request.POST)
            item_details['type'] = request.POST.get('type')
            item_details['title'] = request.POST.get('title')
            item_details['artist'] = request.POST.get('artist')
            item_details['label'] = request.POST.get('label')
            item_details['release_date'] = request.POST.get('release_date')
            item_details['asin'] = request.POST.get('asin')
            item_details['quantity'] = request.POST.get('quantity')
            get_string = "?item_type=Music"
        elif item_type == 'Magazine':
            form = MagazineForm(request.POST)
            item_details['title'] = request.POST.get('title')
            item_details['publisher'] = request.POST.get('publisher')
            item_details['language'] = request.POST.get('language')
            item_details['isbn_10'] = request.POST.get('isbn_10')
            item_details['isbn_13'] = request.POST.get('isbn_13')
            item_details['quantity'] = request.POST.get('quantity')

        loaned = int(get_quantity(item_id)) - int(get_quantity_available(item_id))
        if (int(get_quantity_available(item_id)) > int(request.POST.get('quantity')) and \
            (int(request.POST.get('quantity'))) < loaned) or \
                int(request.POST.get('quantity')) <= 0 or \
                int(request.POST.get('quantity')) < loaned:
            quantity_valid = False
            form.add_error("quantity",'Quantity too low')
        if form.is_valid() and quantity_valid:
            for key in item_details:
                item_details[key].lstrip("0")
            edit_items(item_details, item_type, item_id)
            return HttpResponseRedirect('/admin/items' + get_string)
        else:
            for error in form.errors:
                messages.error(request, form[error].label + " is invalid.")
            return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': item_type, \
            'item_id': item_id})
    else:
        if item_type == 'Book':
            int(item_id)
            data = get_book(item_id)
            data2 = data[0]
            form = BookForm(initial=data2)
            return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Book', \
            'item_id': item_id})
        elif item_type == 'Movie':
            int(item_id)
            data = get_movie(item_id)
            data2 = data[0]
            form = MovieForm(initial=data2)
            return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Movie', \
            'item_id': item_id})
        elif item_type == 'Magazine':
            int(item_id)
            data = get_magazine(item_id)
            data2 = data[0]
            form = MagazineForm(initial=data2)
            return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Magazine', \
            'item_id': item_id})
        elif item_type == 'Music':
            int(item_id)
            data = get_music(item_id)
            data2 = data[0]
            form = MusicForm(initial=data2)
            return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Music', \
            'item_id': item_id})

def get_loan_history(request):
    form = LoanHistoryFilterForm()
    filters = {}
    if request.GET.get('client_id'):
        filters['client_id'] = request.GET.get('client_id')
        form.initial['client_id'] = request.GET.get('client_id')
    if request.GET.get('item_id'):
        filters['item_id'] = request.GET.get('item_id')
        form.initial['item_id'] = request.GET.get('item_id')
    if request.GET.get('return_date'):
        filters['return_date'] = request.GET.get('return_date')
        form.initial['return_date'] = request.GET.get('return_date')
    if request.GET.get('item_type'):
        if request.GET.get('item_type') == 'Any':
            filters['item_type'] = None
        else:
            filters['item_type'] = request.GET.get('item_type')
        form.initial['item_type'] = request.GET.get('item_type')

    loan_history = get_all_loans(filter = filters)
    for loan in loan_history:
        if loan['stock_id'] is not None:
            loan['item_id'] = loan['stock_id'].split('-')[0]        
        else:
            loan['item_id'] = "Removed"
        if (loan['return_date'] < datetime.now()) and (int(loan['state_id']) == 1):
            loan['loan_status'] = 'Late'
        elif(int(loan['state_id']) == 2):
            loan['loan_status'] = 'Returned'
        else:
            loan['loan_status'] = 'Loaned Out'
        loan['type'] = loan['type'].capitalize()
    return render(request, 'biblioteca/admin/loan_history.html', {'loan_history' : loan_history, \
                                                                    'form' : form})

# Filtering functions

def filtered_book(items, request):
    filtered_items = []
    language = request.GET.get('language_filter')
    publisher = request.GET.get('publisher_filter')
    iformat = request.GET.get('format_filter')
    for book in items:
        if (book['language'] == language or language == 'any') and \
                (book['publisher'] == publisher or publisher == 'any') and \
                (book['format'] == iformat or iformat == 'any'):
            filtered_items.append(book)
    return filtered_items

def filtered_magazine(items, request):
    filtered_items = []
    language = request.GET.get('language_filter')
    publisher = request.GET.get('publisher_filter')
    for mag in items:
        if (mag['language'] == language or language == 'any') and \
                (mag['publisher'] == publisher or publisher == 'any'):
            filtered_items.append(mag)
    return filtered_items

def filtered_movie(items, request):
    filtered_items = []
    director = request.GET.get('director_filter')
    language = request.GET.get('language_filter')
    for movie in items:
        if (movie['director'] == director or director == 'any') and \
                (movie['language'] == language or language == 'any'):
            filtered_items.append(movie)
    return filtered_items

def filtered_music(items, request):
    filtered_items = []
    itype = request.GET.get('type_filter')
    label = request.GET.get('label_filter')
    artist = request.GET.get('artist_filter')
    for music in items:
        if (music['type'] == itype or itype == 'any') and \
                (music['label'] == label or label == 'any') and \
                (music['artist'] == artist or artist == 'any'):
            filtered_items.append(music)
    return filtered_items

# errors

def permission_denied(request, exception):
    return render(request, 'biblioteca/errors/403.html', status=403)
