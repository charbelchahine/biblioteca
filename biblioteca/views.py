from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm
from .gateways import addUser, get_all_users
from .auth import authorize_admin

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
                	return HttpResponseRedirect('admin/landing')
                else:
                	return HttpResponseRedirect('landing')
            else:
                return HttpResponseForbidden()
    else:
        if request.user.is_authenticated:
            if(int(request.user.role_id == 1)):
                return HttpResponseRedirect('admin/landing')
            else:
                return HttpResponseRedirect('landing')
        print(request.user.is_authenticated)
        print(request.session.session_key)
        form = LoginForm()
        return render(request, 'biblioteca/login.html', {'form': form})


def end_session(request):
    logout(request)
    return HttpResponseRedirect('/')

def admin_landing(request):
    if not authorize_admin(request):
        return HttpResponseForbidden()
    return render(request, 'biblioteca/admin/landing.html')

def user_landing(request):
    return render(request, 'biblioteca/landing.html')

def register_user(request):
    if not authorize_admin(request):
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            user_details = dict()
            user_details['email'] = request.POST['email']
            user_details['password'] = request.POST['password']
            user_details['f_name'] = request.POST['f_name']
            user_details['l_name'] = request.POST['l_name']
            user_details['address_id'] = request.POST['address_id']
            user_details['phone_num'] = request.POST['phone_num']
            if request.POST['isAdmin']:
                user_details['role_id'] = '1'
            else:
                user_details['role_id'] = '2'
            addUser(user_details)
            return HttpResponseRedirect('/admin/register')

    else:
        form = RegisterForm
        return render(request, 'biblioteca/admin/register_users.html', {'form': form})

def get_users(request):
    if not authorize_admin(request):
        return HttpResponseForbidden()
    users = get_all_users()
    print(users)
    return render(request, 'biblioteca/admin/view_users.html', {'users': users})
