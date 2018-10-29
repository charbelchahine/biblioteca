from .models import cUser
from django.db import connection
from collections import namedtuple
import datetime

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
    dict(zip(columns, row))
    for row in cursor.fetchall()
    ]

def add_user(dictionary):
    print(dictionary)
    curs = connection.cursor()
    curs.execute("CALL new_client(%s, %s, %s, %s, %s, %s, %s)",[dictionary['l_name'], \
        dictionary['f_name'], dictionary['email'], dictionary['address'], int(dictionary['phone_num']), \
        dictionary['password'], int(dictionary['role_id'])])

def insert_item(dictionary, item_type):
    print(dictionary)
    curs = connection.cursor()
    if item_type == 'Book':
        curs.execute("CALL new_book(%s, %s, %s, %s, %s, %s, %s, %s, %s)",[dictionary['title'], \
            dictionary['author'], dictionary['format'], int(dictionary['pages']), dictionary['publisher'], \
                dictionary['language'], dictionary['isbn_10'], dictionary['isbn_13'], dictionary['quantity']])
    elif item_type == 'Movie':
        curs.execute("CALL new_movie(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",[dictionary['title'], \
            dictionary['director'], dictionary['producers'], dictionary['actors'], dictionary['language'], \
            dictionary['subtitles'], dictionary['dubbed'], dictionary['release_date'], int(dictionary['run_time']), dictionary['quantity']])
    elif item_type == 'Magazine':
        curs.execute("CALL new_magazine(%s, %s, %s, %s, %s, %s)",[dictionary['title'], \
            dictionary['publisher'], dictionary['language'], dictionary['isbn_10'], dictionary['isbn_13'], dictionary['quantity']])
    elif item_type == 'Music':
        curs.execute("CALL new_music(%s, %s, %s, %s, %s, %s, %s)",[dictionary['type'], \
            dictionary['title'], dictionary['artist'], dictionary['label'], dictionary['release_date'], dictionary['asin'], dictionary['quantity']])

def delete_item(idToDelete):
    print(idToDelete)
    curs = connection.cursor()
    curs.execute("CALL delete_item(%s)",[int(idToDelete)])

def get_all_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT clients.loan_item_count, clients.user_id, clients.f_name, clients.l_name, clients.address, clients.phone_num, clients.last_visited, users.email, has_role.role_id, auth.password, roles.name\
                FROM clients, users, has_role, auth, roles\
                WHERE has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id AND clients.user_id = users.id")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    print(row)
    return row
def update_user(**kwargs):
    update_params = ""
    for key, value in kwargs.items():
        if key is not "user_id":
            update_params = update_params + \
            str(key) + " = " + "'" + str(value) + "'" + ", "
    update_params = update_params[:-2]
    query = "UPDATE clients SET " + update_params + " WHERE user_id = " + str(kwargs.get('user_id')) +  ";"
    curs = connection.cursor()
    curs.execute(query)
    print(query)

def get_all_items(item_type):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM items i \
                WHERE i.type = \"" + item_type + "\";")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row           

def get_books\
(id=None, author = None, format = None, pages=None, publisher=None, isbn_10=None, \
    isbn_13=None):
    query = 'SELECT books.*, items.quantity \
        FROM books, items \
        WHERE books.id = items.id'
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row 

def get_book(item_id=None):
    with connection.cursor() as cursor:
        cursor.execute('SELECT books.*, items.quantity FROM books, items \
        WHERE books.id = items.id AND items.id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_movies\
(id=None, title=None, director=None, producers=None, actors=None, language=None, \
    subtitles=None, dubbed = None, release_date = None, run_time = None):
    query = 'SELECT movies.*, items.quantity \
        FROM movies, items \
        WHERE movies.id = items.id'
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row 

def get_movie(item_id=None):
    with connection.cursor() as cursor:
        cursor.execute('SELECT movies.*, items.quantity FROM movies, items \
        WHERE movies.id = items.id AND items.id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_magazines\
(id = None, title = None, publisher = None, language = None, isbn_10 = None, \
    isbn_13 = None):
    query = 'SELECT magazines.*, items.quantity \
        FROM magazines, items \
        WHERE magazines.id = items.id'
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row 

def get_magazine(item_id=None):
    with connection.cursor() as cursor:
        cursor.execute('SELECT magazines.*, items.quantity FROM magazines, items \
        WHERE magazines.id = items.id AND items.id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_musics\
(id = None, type = None, title = None, artist = None, label = None, \
    release_date = None, asin=None):
    query = 'SELECT music.*, items.quantity \
        FROM music, items \
        WHERE music.id = items.id'
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row 

def get_music(item_id=None):
    with connection.cursor() as cursor:
        cursor.execute('SELECT music.*, items.quantity FROM music, items \
        WHERE music.id = items.id AND items.id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def unique_email(email):
    with connection.cursor() as c:
        c.execute('SELECT COUNT(email) FROM users WHERE email = %s', [email])
        data = c.fetchone()
    return int(data[0]) < 1


def edit_items(dictionary, item_type, item_id):
    print(dictionary)
    curs = connection.cursor()
    if item_type == 'Book':
        curs.execute("UPDATE books, items \
        SET books.title = %s, books.author = %s, books.format = %s, books.pages = %s, books.publisher = %s, \
        books.language = %s, books.isbn_10 = %s, books.isbn_13 = %s, items.quantity = %s \
        WHERE books.id= %s AND items.id = books.id", [dictionary['title'], dictionary['author'], dictionary['format'], \
        dictionary['pages'], dictionary['publisher'], dictionary['language'], \
        dictionary['isbn_10'], dictionary['isbn_13'], dictionary['quantity'], item_id])
    elif item_type == 'Movie':
        curs.execute("UPDATE movies, items \
        SET movies.title = %s, movies.director = %s, movies.producers = %s, movies.actors = %s, movies.language = %s, \
        movies.subtitles = %s, movies.dubbed = %s, movies.release_date = %s, movies.run_time = %s, items.quantity = %s \
        WHERE movies.id= %s AND items.id = movies.id", [dictionary['title'], dictionary['director'], dictionary['producers'], \
        dictionary['actors'], dictionary['language'], dictionary['subtitles'], \
        dictionary['dubbed'], dictionary['release_date'], dictionary['run_time'], dictionary['quantity'], item_id])
    elif item_type == 'Magazine':
        curs.execute("UPDATE magazines, items \
        SET magazines.title = %s, magazines.publisher = %s, magazines.language = %s, magazines.isbn_10 = %s, \
        magazines.isbn_13 = %s, items.quantity = %s \
        WHERE magazines.id = %s AND items.id = magazines.id", [dictionary['title'], dictionary['publisher'], dictionary['language'], \
        dictionary['isbn_10'], dictionary['isbn_13'], dictionary['quantity'], item_id])
    elif item_type == 'Music':
        curs.execute("UPDATE music, items \
        SET music.type = %s, music.title = %s, music.artist = %s, music.label = %s, music.release_date = %s, \
        music.asin = %s, items.quantity = %s \
        WHERE music.id= %s AND items.id = music.id", [dictionary['type'], dictionary['title'], dictionary['artist'], \
        dictionary['label'], dictionary['release_date'], dictionary['asin'], dictionary['quantity'], item_id])


def get_vtk_log():
    print('---------------')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM django_user_log;")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row

def edit_vtk_log(name):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE django_user_log SET vote_count = vote_count + 1 WHERE user_name = %s;", [name])

