from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, EditItem
from .gateways import add_user, get_all_users, get_all_items, get_all_properties, \
    get_magazines, get_movies, get_musics, get_books, edit_properties
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
        if form.is_valid:
            user_details = dict()
            user_details['email'] = request.POST.get('email')
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
        return render(request, 'biblioteca/admin/register_users.html', {'form': form})

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

def edit_item(request):
    if not authorize_admin(request):
        raise PermissionDenied
    if request.method == 'POST':
        form = EditItem(request.POST)
        if form.is_valid:
            item_details = dict()
            item_details['email'] = request.POST.get('email')
            edit_properties(item_details)
            return HttpResponseRedirect('/admin/items')

    else:
        form = EditItem
        return render(request, 'biblioteca/admin/edit_item.html', {'form': form })

# errors

def permission_denied(request, exception):
    return render(request, 'biblioteca/errors/403.html', status=403)