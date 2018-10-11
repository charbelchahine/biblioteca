from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, BookForm, MovieForm, MusicForm, MagazineForm
from .gateways import add_user, get_all_users, get_all_items, get_all_properties, \
    get_magazines, get_movies, get_musics, get_books, insert_item, unique_email, \
    edit_properties, get_book, get_movie, get_magazine, get_music
from .auth import authorize_admin
from django.shortcuts import redirect

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
                	return HttpResponseRedirect('landing')
            else:
                return redirect('login')
    else:
        if request.user.is_authenticated:
            if(int(request.user.role_id == 1)):
                return HttpResponseRedirect('admin')
            else:
                return HttpResponseRedirect('landing')
        print(request.user.is_authenticated)
        print(request.session.session_key)
        form = LoginForm()
        return render(request, 'biblioteca/login.html', {'form': form})


def end_session(request):
    logout(request)
    return HttpResponseRedirect('/')

# Client stuff

def client_landing(request):
    return render(request, 'biblioteca/landing.html')

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
        user_details = dict()
        user_details['email'] = request.POST.get('email')
        if unique_email(user_details['email']) == False:
            error = 'Provided email is not valid because it is not unique. The provided email already exists in the System.'
            return render(request, 'biblioteca/admin/register_users.html', {'form': form, 'error': error})
        if form.is_valid:
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
            if form.is_valid:
                item_details['title'] = request.POST.get('title')
                item_details['author'] = request.POST.get('author')
                item_details['format'] = request.POST.get('format')
                item_details['pages'] = request.POST.get('pages')
                item_details['publisher'] = request.POST.get('publisher')
                item_details['language'] = request.POST.get('language')
                item_details['isbn_10'] = request.POST.get('isbn_10')
                item_details['isbn_13'] = request.POST.get('isbn_13')
        elif item_type == 'Movie':
            form = MovieForm(request.POST)
            if form.is_valid:
                item_details['title'] = request.POST.get('title')
                item_details['director'] = request.POST.get('director')
                item_details['producers'] = request.POST.get('producers')
                item_details['actors'] = request.POST.get('actors')
                item_details['language'] = request.POST.get('language')
                item_details['subtitles'] = request.POST.get('subtitles')
                item_details['dubbed'] = request.POST.get('dubbed')
                item_details['release_date'] = request.POST.get('release_date')
                item_details['run_time'] = request.POST.get('run_time')
        elif item_type == 'Music':
            form = MusicForm(request.POST)
            if form.is_valid:
                item_details = dict()
                item_details['type'] = request.POST.get('type')
                item_details['title'] = request.POST.get('title')
                item_details['artist'] = request.POST.get('artist')
                item_details['label'] = request.POST.get('label')
                item_details['release_date'] = request.POST.get('release_date')
                item_details['asin'] = request.POST.get('asin')
        elif item_type == 'Magazine':
            form = MagazineForm(request.POST)
            if form.is_valid:
                item_details = dict()
                item_details['title'] = request.POST.get('title')
                item_details['publisher'] = request.POST.get('publisher')
                item_details['language'] = request.POST.get('language')
                item_details['isbn_10'] = request.POST.get('isbn_10')
                item_details['isbn_13'] = request.POST.get('isbn_13')
        insert_item(item_details, item_type) 
        return HttpResponseRedirect('/admin/add_item/' + item_type)
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


def get_users(request):
    if not authorize_admin(request):
        raise PermissionDenied
    users = get_all_users()
    print(users)
    return render(request, 'biblioteca/admin/view_users.html', {'users': users})

def get_items(request):
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            item_type = request.POST.get('item_type')
        else:
            item_type = 'Magazine'
    else:
        item_type = 'Magazine'
    print(item_type)
    
    if item_type == "Magazine":
        items = get_magazines()
    if item_type == "Book":
        items = get_books()
    if item_type == "Music":
        items = get_musics()
    if item_type == "Movie":
        items = get_movies()
    print(items)
    return render(request, 'biblioteca/admin/view_items.html', {'items': items, 'item_type': item_type})  

def edit_item(request, item_type = None, item_id=None):
    if not authorize_admin(request):
        raise PermissionDenied
    if item_type == 'Book':
        int(item_id)
        data = get_book(item_id)
        data2 = data[0]
        form = EditBook(initial=data2)
        return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Book', \
         'item_id': item_id})
    elif item_type == 'Movie':
        int(item_id)
        data = get_movie(item_id)
        data2 = data[0]
        form = EditMovie(initial=data2)
        return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Movie', \
        'item_id': item_id})
    elif item_type == 'Magazine':
        int(item_id)
        data = get_magazine(item_id)
        data2 = data[0]
        form = EditMagazine(initial=data2)
        return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Magazine', \
        'item_id': item_id})
    elif item_type == 'Music':
        int(item_id)
        data = get_music(item_id)
        data2 = data[0]
        form = EditMusic(initial=data2)
        return render(request, 'biblioteca/admin/edit_item.html', {'form': form, 'item_type': 'Music', \
        'item_id': item_id})

# errors

def permission_denied(request, exception):
    return render(request, 'biblioteca/errors/403.html', status=403)
