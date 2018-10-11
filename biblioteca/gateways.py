from .models import cUser
from django.db import connection
from collections import namedtuple

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
    dict(zip(columns, row))
    for row in cursor.fetchall()
    ]

def add_user(dictionary):
    print(dictionary)
    curs = connection.cursor()
    curs.execute("CALL new_client(%s, %s, %s, %s, %s, %s, %s)",[dictionary['l_name'], dictionary['f_name'], dictionary['email'], dictionary['address'], int(dictionary['phone_num']), dictionary['password'], int(dictionary['role_id'])])


def get_all_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT clients.loan_item_count, clients.user_id, clients.f_name, clients.l_name, clients.address, clients.phone_num, users.email, has_role.role_id, auth.password, roles.name\
                FROM clients, users, has_role, auth, roles\
                WHERE has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id AND clients.user_id = users.id")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    print(row)
    return row

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

def get_all_properties(item_type):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM items i \
                INNER JOIN item_properties ip on i.id = ip.item_id \
                WHERE i.type = \"" + item_type + "\" \
                ORDER BY i.id;")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row            

def get_books\
(id=None, author = None, format = None, pages=None, publisher=None, isbn_10=None, \
    isbn_13=None):
    query = 'SELECT * FROM books'
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
        cursor.execute('SELECT * FROM books WHERE id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_movies\
(id=None, title=None, director=None, producers=None, actors=None, language=None, \
    subtitles=None, dubbed = None, release_date = None, run_time = None):
    query = 'SELECT * FROM movies'
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
        cursor.execute('SELECT * FROM movies WHERE id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_magazines\
(id = None, title = None, publisher = None, language = None, isbn_10 = None, \
    isbn_13 = None):
    query = 'SELECT * FROM magazines'
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
        cursor.execute('SELECT * FROM magazines WHERE id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def get_musics\
(id = None, type = None, title = None, artist = None, label = None, \
    release_date = None, asin=None):
    query = 'SELECT * FROM music'
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
        cursor.execute('SELECT * FROM music WHERE id = %s', [item_id])
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

def edit_properties(dictionary, item_type):
    print(dictionary)
    curs = connection.cursor()
    if item_type == 'Book':
        curs.execute("")
    elif item_type == 'Movie':
        curs.execute("")
    elif item_type == 'Magazine':
        curs.execute("")
    elif item_type == 'Music':
        curs.execute("")


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

