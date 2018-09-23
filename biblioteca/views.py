from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .gateways import userGateway
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def index(request):
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
                login(request, user)
                if user.role_id==1:
                	return render(request, 'biblioteca/admin/landing.html')
                else:
                	return render(request, 'biblioteca/landing.html')
            else:
                print("=========NOT USER==========")
    else:
        form = LoginForm()
        return render(request, 'biblioteca/login.html', {'form': form})

	
