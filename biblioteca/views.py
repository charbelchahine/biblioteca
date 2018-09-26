from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from .gateways import userGateway
from django.contrib.auth import login, logout
from .forms import LoginForm
from .common import checkUser

def index(request):
    print(request.user.is_authenticated)
    return render(request, 'biblioteca/index.html')

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = userGateway(username,password)
            if user is not None:
                print("=========USER==========")
                print(user.email)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user, user.backend)
                print(request.user.is_authenticated)
                if request.user.role_id==1:
                    return render(request, 'biblioteca/admin/landing.html')
                	# return HttpResponseRedirect('/')
                else:
                	return render(request, 'biblioteca/landing.html')
            else:
                print("=========NOT USER==========")
    else:
        if request.user.is_authenticated:
            return render(request, 'biblioteca/admin/landing.html')
        print(request.user.is_authenticated)
        form = LoginForm()
        return render(request, 'biblioteca/login.html', {'form': form})


def end_session(request):
    logout(request)
    return HttpResponseRedirect('/')

def admin_landing(request):
    return render(request, 'biblioteca/admin/landing.html')