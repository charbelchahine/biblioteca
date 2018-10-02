from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	email = forms.CharField(label='Email', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
	isAdmin = forms.BooleanField(required=False, label="Admin")
	f_name = forms.CharField(label="First Name", max_length=100)
	l_name = forms.CharField(label="Last Name", max_length=100)
	address = forms.CharField(label="Address", max_length=100)
	phone_num = forms.IntegerField(label="Phone Number")
