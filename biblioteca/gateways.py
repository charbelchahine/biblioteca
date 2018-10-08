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

def delete_item(dictionary):
    print(dictionary)
    curs = connection.cursor()
    curs.execute("CALL delete_item(%s)",[dictionary['item_id']])

def get_all_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT *\
FROM clients LEFT JOIN (SELECT users.id, has_role.role_id, auth.password, roles.name\
                FROM users, has_role, auth, roles\
                where has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id) as sq1 ON (sq1.id = clients.user_id);") # Thank you Matt for this amazing query
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

def get_musics\
(id = None, type = None, title = None, artist = None, label = None, \
    release_date = None, asin=None):
    query = 'SELECT * FROM magazines'
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row 

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

