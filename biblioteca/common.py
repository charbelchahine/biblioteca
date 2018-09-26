from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from .gateways import userGateway
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def checkUser(request):
	return (request.user is not None and not request.user.is_anonymous)