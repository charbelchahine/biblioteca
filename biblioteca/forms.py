from django import forms
import datetime

class LoginForm(forms.Form):
    username = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    email = forms.RegexField(label='Email', regex=r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+$")
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
    pages = forms.RegexField(label='Pages', regex=r'^0*[0-4]{0,1}\d{1,3}$')
    publisher = forms.CharField(label='Publisher', max_length=100)
    language = forms.CharField(label='Language', max_length=100)
    isbn_10 = forms.CharField(label='ISBN-10', max_length=100)
    isbn_13 = forms.CharField(label='ISBN-13', max_length=100)
    quantity = forms.RegexField(label='Quantity', regex=r'^0*[1-9]+\d*$')

class MovieForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    director = forms.CharField(label='Director', max_length=100)
    producers = forms.CharField(label='Producers', max_length=100)
    actors = forms.CharField(label='Actors', max_length=100)
    language = forms.CharField(label='Language', max_length=100)
    subtitles = forms.CharField(label='Subtitles', max_length=100)
    dubbed = forms.CharField(label='Dubbed', max_length=100)
    release_date = forms.DateField(label='Release Date', initial=datetime.date.today, input_formats=['%Y-%m-%d'])
    run_time = forms.RegexField(label='Run Time', regex=r'^0*[0-5]{0,1}\d{1,4}$')
    quantity = forms.RegexField(label='Quantity', regex=r'^0*[1-9]+\d*$')

class MusicForm(forms.Form):
    type = forms.CharField(label='Type', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    artist = forms.CharField(label='Artist', max_length=100)
    label = forms.CharField(label='Label', max_length=100)
    release_date = forms.DateField(label='Release Date', initial=datetime.date.today, input_formats=['%Y-%m-%d'])
    asin = forms.CharField(label='ASIN', max_length=100)
    quantity = forms.RegexField(label='Quantity', regex=r'^0*[1-9]+\d*$')

class MagazineForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    publisher = forms.CharField(label='Publisher', max_length=100)
    language = forms.CharField(label='Language', max_length=100)
    isbn_10 = forms.CharField(label='ISBN-10', max_length=100)
    isbn_13 = forms.CharField(label='ISBN-13', max_length=100)
    quantity = forms.RegexField(label='Quantity', regex=r'^0*[1-9]+\d*$')

class ItemSelectorForm(forms.Form):
    item_type = forms.ChoiceField(label='Item Type',
                                  choices=[("Magazine", "Magazine"), ("Book", "Book"), ("Movie", "Movie"),
                                           ("Music", "Music")])

class ItemSortingForm(forms.Form):
    # This extra stuff here is to be able to pass an argument to ItemSortingForm()
    def __init__(self, sorting_options, *args, **kwargs):
        super(ItemSortingForm, self).__init__(*args, **kwargs)
        self.fields['sort_by'] = forms.ChoiceField(label='Sort by',
                                                   choices=tuple([(option, option) for option in sorting_options]))

    class Meta:
        fields = ('name',)

class BookFilterForm(forms.Form):
    def __init__(self, language_options, publisher_options, format_options, *args, **kwargs):
        super(BookFilterForm, self).__init__(*args, **kwargs)
        choices = [('any', 'any')]
        for option in language_options:
            choices.append((option, option))
        self.fields['language_filter'] = forms.ChoiceField(label='Language', choices=choices)
        choices = [('any', 'any')]
        for option in publisher_options:
            choices.append((option, option))
        self.fields['publisher_filter'] = forms.ChoiceField(label='Publisher', choices=choices)
        choices = [('any', 'any')]
        for option in format_options:
            choices.append((option, option))
        self.fields['format_filter'] = forms.ChoiceField(label='Format', choices=choices)

    class Meta:
        fields = ('languages', 'publishers', 'formats')

class MagazineFilterForm(forms.Form):
    def __init__(self, language_options, publisher_options, *args, **kwargs):
        super(MagazineFilterForm, self).__init__(*args, **kwargs)
        choices = [('any', 'any')]
        for option in language_options:
            choices.append((option, option))
        self.fields['language_filter'] = forms.ChoiceField(label='Language', choices=choices)
        choices = [('any', 'any')]
        for option in publisher_options:
            choices.append((option, option))
        self.fields['publisher_filter'] = forms.ChoiceField(label='Publisher', choices=choices)

    class Meta:
        fields = ('languages', 'publishers',)

class MusicFilterForm(forms.Form):
    def __init__(self, type_options, label_options, artist_options, *args, **kwargs):
        super(MusicFilterForm, self).__init__(*args, **kwargs)
        choices = [('any', 'any')]
        for option in type_options:
            choices.append((option, option))
        self.fields['type_filter'] = forms.ChoiceField(label='Type', choices=choices)
        choices = [('any', 'any')]
        for option in label_options:
            choices.append((option, option))
        self.fields['label_filter'] = forms.ChoiceField(label='Label', choices=choices)
        choices = [('any', 'any')]
        for option in artist_options:
            choices.append((option, option))
        self.fields['artist_filter'] = forms.ChoiceField(label='Artist', choices=choices)

    class Meta:
        fields = ('types', 'labels', 'artists',)

class MovieFilterForm(forms.Form):
    def __init__(self, director_options, language_options, *args, **kwargs):
        super(MovieFilterForm, self).__init__(*args, **kwargs)
        choices = [('any', 'any')]
        for option in director_options:
            choices.append((option, option))
        self.fields['director_filter'] = forms.ChoiceField(label='Director', choices=choices)
        choices = [('any', 'any')]
        for option in language_options:
            choices.append((option, option))
        self.fields['language_filter'] = forms.ChoiceField(label='Language', choices=choices)

    class Meta:
        fields = ('directors', 'labels',)

class LoanHistoryFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoanHistoryFilterForm, self).__init__(*args, **kwargs)
        self.fields['client_id'] = forms.CharField(label='Client ID', required=False)
        self.fields['item_id'] = forms.CharField(label='Item ID', required=False)
        self.fields['return_date'] = forms.DateField(label='Due Date (YYYY-MM-DD)', required=False)
        self.fields['item_type'] = forms.ChoiceField(label='Item Type', choices=[('', 'Any'), ('Book', 'Book'), \
                                                    ('Movie', 'Movie'), ('Music', 'Music')], required=False)
