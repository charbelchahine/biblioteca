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

class BookForm(forms.Form):
	book_id = forms.IntegerField(label="ID")
	title = forms.CharField(label='Title', max_length=100)
	author = forms.CharField(label='Author', max_length=100)
	format = forms.CharField(label='Format', max_length=100)
	pages = forms.IntegerField(label='Pages')
	publisher = forms.CharField(label='Publisher', max_length=100)
	language = forms.CharField(label='Language', max_length=100)
	isbn_10 = forms.CharField(label='ISBN-10', max_length=100)
	isbn_13 = forms.CharField(label='ISBN-13', max_length=100)

