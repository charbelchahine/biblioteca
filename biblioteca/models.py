from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now

# Create your models here.

class cUser(AbstractBaseUser):
    def save(self, *args, **kwargs):
        pass
    role_id = models.IntegerField()
    user_id = models.IntegerField()
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone_num = models.IntegerField()
    loan_item_count = models.IntegerField()
    last_visited = models.DateTimeField()
    id = models.IntegerField(unique = True, primary_key = True)

    def __init__(self, dictionary, *args, **kwargs):
        self.role_id = int(dictionary['role_id'])
        self.user_id = dictionary['user_id']
        self.email = dictionary['email']
        self.password = dictionary['password']
        self.f_name = dictionary['f_name']
        self.l_name = dictionary['l_name']
        self.address = dictionary['address']
        self.phone_num = dictionary['phone_num']
        self.loan_item_count = dictionary['loan_item_count']
        self.last_visited = dictionary['last_visited']
        self.id = self.user_id

    USERNAME_FIELD = 'id'
    class Meta:
        managed = False

class cItem(models.Model):
    item_id = models.IntegerField()
    item_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rental_duration = models.IntegerField()
    item_property = models.CharField(max_length=75)
    item_name = models.CharField(max_length=250)

class Book(models.Model):
    def save(self, *args, **kwargs):
        pass
    id = models.IntegerField(unique = True, primary_key = True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    format = models.CharField(max_length=40)
    pages = models.IntegerField()
    publisher = models.CharField(max_length = 40)
    language = models.CharField(max_length = 40)
    isbn_10 = models.CharField(max_length = 40)
    isbn_13 = models.CharField(max_length = 40)

    def __init__(self, dictionary, *args, **kwargs):
        self.id = int(dictionary['id'])
        self.title = dictionary['title']
        self.author = dictionary['author']
        self.format = dictionary['format']
        self.pages = dictionary['pages']
        self.publisher = dictionary['publisher']
        self.language = dictionary['language']
        self.isbn_13 = dictionary['isbn_13']
        self.isbn_10 = dictionary['isbn_10']
    class Meta:
        managed = False

class Movie(models.Model):
    def save(self, *args, **kwargs):
        pass
    id = models.IntegerField(unique = True, primary_key = True)
    title = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    producers = models.CharField(max_length=40)
    actors = models.CharField(max_length = 100)
    subtitles = models.CharField(max_length = 40)
    language = models.CharField(max_length = 40)
    dubbed = models.CharField(max_length = 40)
    release_date = models.DateField()
    run_time = models.IntegerField()

    def __init__(self, dictionary, *args, **kwargs):
        self.id = int(dictionary['id'])
        self.title = dictionary['title']
        self.director = dictionary['director']
        self.producers = dictionary['producers']
        self.actors = dictionary['actors']
        self.subtitles = dictionary['subtitles']
        self.language = dictionary['language']
        self.dubbed = dictionary['dubbed']
        self.release_date = dictionary['release_date']
        self.run_time = dictionary['run_time']

    class Meta:
        managed = False

class Magazine(models.Model):
    def save(self, *args, **kwargs):
        pass
    id = models.IntegerField(unique = True, primary_key = True)
    title = models.CharField(max_length = 40)
    publisher = models.CharField(max_length = 40)
    language = models.CharField(max_length = 40)
    isbn_10 = models.CharField(max_length = 40)
    isbn_13 = models.CharField(max_length = 40)

    def __init__(self, dictionary, *args, **kwargs):
        self.id = int(dictionary['id'])
        self.title =  dictionary['title']
        self.publisher = dictionary['publisher']
        self.language = dictionary['language']
        self.isbn_10 = dictionary['isbn_10']
        self.isbn_13 = dictionary['isbn_13']

    class Meta:
        managed = False

class Music(models.Model):
    def save(self, *args, **kwargs):
        pass
    id = models.IntegerField(unique = True, primary_key = True)
    type = models.CharField(max_length = 40)
    title = models.CharField(max_length = 40)
    artist = models.CharField(max_length = 40)
    label = models.CharField(max_length = 40)
    release_date = models.DateField()
    asin = models.CharField(max_length = 40)

    def __init__(self, dictionary, *args, **kwargs):
        self.id = int(dictionary['id'])
        self.type = dictionary['type']
        self.title = dictionary['title']
        self.artist = dictionary['artist']
        self.label = dictionary['label']
        self.release_date = dictionary['release_date']
        self.asin = dictionary['asin']
    class Meta:
        managed = False