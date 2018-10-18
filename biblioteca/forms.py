from django import forms
import datetime

class LoginForm(forms.Form):
	username = forms.CharField(label='Email', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
	isAdmin = forms.BooleanField(required=False, label="Admin")
	f_name = forms.CharField(label="First Name", max_length=100)
	l_name = forms.CharField(label="Last Name", max_length=100)
	address = forms.CharField(label="Address", max_length=100)
	phone_num = forms.IntegerField(min_value=10000, max_value=999999999999999, label="Phone Number")

class BookForm(forms.Form):
	title = forms.CharField(label='Title', max_length=100)
	author = forms.CharField(label='Author', max_length=100)
	format = forms.CharField(label='Format', max_length=100)
	pages = forms.IntegerField(label='Pages')
	publisher = forms.CharField(label='Publisher', max_length=100)
	language = forms.CharField(label='Language', max_length=100)
	isbn_10 = forms.CharField(label='ISBN-10', max_length=100)
	isbn_13 = forms.CharField(label='ISBN-13', max_length=100)
	quantity = forms.IntegerField(label='Quantity')


class MovieForm(forms.Form):
	title = forms.CharField(label='Title', max_length=100)
	director = forms.CharField(label='Director', max_length=100)
	producers = forms.CharField(label='Producers', max_length=100)
	actors = forms.CharField(label='Actors', max_length=100)
	language = forms.CharField(label='Language', max_length=100)
	subtitles = forms.CharField(label='Subtitles', max_length=100)
	dubbed = forms.CharField(label='Dubbed', max_length=100)
	release_date = forms.DateField(label='Release Date', initial=datetime.date.today)
	run_time = forms.IntegerField(label='Run Time')
	quantity = forms.IntegerField(label='Quantity')

class MusicForm(forms.Form):
	type = forms.CharField(label='Type', max_length=100)
	title = forms.CharField(label='Title', max_length=100)
	artist = forms.CharField(label='Artist', max_length=100)
	label = forms.CharField(label='Label', max_length=100)
	release_date = forms.DateField(label='Release Date', initial=datetime.date.today)
	asin = forms.CharField(label='ASIN', max_length=100)
	quantity = forms.IntegerField(label='Quantity')

class MagazineForm(forms.Form):
	title = forms.CharField(label='Title', max_length=100)
	publisher = forms.CharField(label='Publisher', max_length=100)
	language = forms.CharField(label='Language', max_length=100)
	isbn_10 = forms.CharField(label='ISBN-10', max_length=100)
	isbn_13 = forms.CharField(label='ISBN-13', max_length=100)
	quantity = forms.IntegerField(label='Quantity')

class ItemSelectorForm(forms.Form):
        category = forms.ChoiceField(label='Category', choices = [("1","Magazine"), ("2","Book"), ("3","Movie"), ("4","Music")])
