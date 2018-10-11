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

class EditBook(forms.Form):
	id = forms.CharField(disabled=True)
	title = forms.CharField(label='Title', max_length=100, initial='')
	author = forms.CharField(label='Author', max_length=100, initial='')
	format = forms.CharField(label='Format', max_length=100, initial='')
	pages = forms.IntegerField(label='Pages', initial='')
	publisher = forms.CharField(label='Publisher', max_length=100, initial='')
	language = forms.CharField(label='Language', max_length=100, initial='')
	isbn_10 = forms.CharField(label='ISBN-10', max_length=100, initial='')
	isbn_13 = forms.CharField(label='ISBN-13', max_length=100, initial='')

class EditMovie(forms.Form):
	title = forms.CharField(label='Title', max_length=100, initial='')
	director = forms.CharField(label='Director', max_length=100, initial='')
	producers = forms.CharField(label='Producers', max_length=100, initial='')
	actors = forms.CharField(label='Actors', max_length=100, initial='')
	language = forms.CharField(label='Language', max_length=100, initial='')
	subtitles = forms.CharField(label='Subtitles', max_length=100, initial='')
	dubbed = forms.CharField(label='Dubbed', max_length=100, initial='')
	release_date = forms.DateField(label='Release Date', initial='')
	run_time = forms.IntegerField(label='Run Time', initial='')

class EditMusic(forms.Form):
	type = forms.CharField(label='Type', max_length=100, initial='')
	title = forms.CharField(label='Title', max_length=100, initial='')
	artist = forms.CharField(label='Artist', max_length=100, initial='')
	label = forms.CharField(label='Label', max_length=100, initial='')
	release_date = forms.DateField(label='Release Date', initial='')
	asin = forms.CharField(label='ASIN', max_length=100, initial='')

class EditMagazine(forms.Form):
	title = forms.CharField(label='Title', max_length=100, initial='')
	publisher = forms.CharField(label='Publisher', max_length=100, initial='')
	language = forms.CharField(label='Language', max_length=100, initial='')
	isbn_10 = forms.CharField(label='ISBN-10', max_length=100, initial='')
	isbn_13 = forms.CharField(label='ISBN-13', max_length=100, initial='')