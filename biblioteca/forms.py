from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	email = forms.CharField(label='Email', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
	isAdmin = forms.BooleanField(required=False, label="Admin")
	f_name = forms.CharField(label="first name", max_length=100)
	l_name = forms.CharField(label="last name", max_length=100)
	address_id = forms.IntegerField(label="Address ID")
	phone_num = forms.IntegerField(label="Phone Number")
