from .models import cUser
from .string_utils import serialize, deserialize
from django.db import connection
from collections import namedtuple
import random
import string
import datetime
from django.utils.timezone import now
from contracts import contract

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
        curs.execute("CALL new_book(%s, %s, %s, %s, %s, %s, %s, %s, 0)",[dictionary['title'], \
            dictionary['author'], dictionary['format'], int(dictionary['pages']), dictionary['publisher'], \
                dictionary['language'], dictionary['isbn_10'], dictionary['isbn_13']])
    elif item_type == 'Movie':
        curs.execute("CALL new_movie(%s, %s, %s, %s, %s, %s, %s, %s, %s, 0)",[dictionary['title'], \
            dictionary['director'], dictionary['producers'], dictionary['actors'], dictionary['language'], \
            dictionary['subtitles'], dictionary['dubbed'], dictionary['release_date'], int(dictionary['run_time'])])
    elif item_type == 'Magazine':
        curs.execute("CALL new_magazine(%s, %s, %s, %s, %s, 0)",[dictionary['title'], \
            dictionary['publisher'], dictionary['language'], dictionary['isbn_10'], dictionary['isbn_13']])
    elif item_type == 'Music':
        curs.execute("CALL new_music(%s, %s, %s, %s, %s, %s, 0)",[dictionary['type'], \
            dictionary['title'], dictionary['artist'], dictionary['label'], dictionary['release_date'], dictionary['asin']])
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM items ORDER BY id DESC LIMIT 1;")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
        item_id = row[0]['id']
    increase_quantity(int(dictionary['quantity']), item_type, item_id)

def id_generator(item_id, size=5, chars=string.ascii_uppercase + string.digits):
    serial_num = ''.join(random.choice(chars) for _ in range(size))
    print(serial_num)
    item_id = str(item_id) + '-' + serial_num
    return item_id

def increase_quantity(quantity_diff, item_type, item_id):
    curs = connection.cursor()
    for x in range(0, quantity_diff):
        stock_id = id_generator(item_id)
        curs.execute("INSERT INTO inventory VALUES (%s, %s, NULL)", [item_id, stock_id])

def decrease_quantity(quantity_diff, item_type, item_id):
    curs = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM inventory \
                WHERE inventory.item_id = %s AND inventory.loan_id IS NULL", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    unloaned_items = row
    if quantity_diff > len(unloaned_items):
        pass
    for x in range(0, quantity_diff):
        curs.execute("UPDATE loans SET stock_id = NULL WHERE stock_id = %s AND state_id = 2", [unloaned_items[x]['stock_id']])
    for x in range(0, quantity_diff):
        curs.execute("DELETE FROM inventory WHERE inventory.stock_id = %s", [unloaned_items[x]['stock_id']])

def delete_item(idToDelete):
    print(idToDelete)
    curs = connection.cursor()
    curs.execute("CALL delete_item(%s)",[int(idToDelete)])

def get_all_loaned_item_instances(item_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM inventory WHERE inventory.item_id = %s AND \
                        inventory.loan_id IS NOT NULL", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return row

def get_all_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT clients.loan_item_count, clients.user_id, clients.f_name, clients.l_name, \
                clients.address, clients.phone_num, clients.last_visited, users.email, has_role.role_id, auth.password, roles.name \
                FROM clients, users, has_role, auth, roles \
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
    query = 'SELECT books.*, items.quantity, items.quantity_available \
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
    query = 'SELECT movies.*, items.quantity, items.quantity_available \
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
    query = 'SELECT magazines.*, items.quantity, items.quantity_available \
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
    query = 'SELECT music.*, items.quantity, items.quantity_available \
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
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE id = %s", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    old_quantity = int(row[0]['quantity'])
    new_quantity = int(dictionary['quantity'])
    quantity_diff = new_quantity - old_quantity
    curs = connection.cursor()
    if item_type == 'Book':
        curs.execute("UPDATE books, items \
        SET books.title = %s, books.author = %s, books.format = %s, books.pages = %s, books.publisher = %s, \
        books.language = %s, books.isbn_10 = %s, books.isbn_13 = %s \
        WHERE books.id= %s AND items.id = books.id", [dictionary['title'], dictionary['author'], dictionary['format'], \
        dictionary['pages'], dictionary['publisher'], dictionary['language'], \
        dictionary['isbn_10'], dictionary['isbn_13'], item_id])
    elif item_type == 'Movie':
        curs.execute("UPDATE movies, items \
        SET movies.title = %s, movies.director = %s, movies.producers = %s, movies.actors = %s, movies.language = %s, \
        movies.subtitles = %s, movies.dubbed = %s, movies.release_date = %s, movies.run_time = %s \
        WHERE movies.id= %s AND items.id = movies.id", [dictionary['title'], dictionary['director'], dictionary['producers'], \
        dictionary['actors'], dictionary['language'], dictionary['subtitles'], \
        dictionary['dubbed'], dictionary['release_date'], dictionary['run_time'], item_id])
    elif item_type == 'Magazine':
        curs.execute("UPDATE magazines, items \
        SET magazines.title = %s, magazines.publisher = %s, magazines.language = %s, magazines.isbn_10 = %s, \
        magazines.isbn_13 = %s \
        WHERE magazines.id = %s AND items.id = magazines.id", [dictionary['title'], dictionary['publisher'], dictionary['language'], \
        dictionary['isbn_10'], dictionary['isbn_13'], item_id])
    elif item_type == 'Music':
        curs.execute("UPDATE music, items \
        SET music.type = %s, music.title = %s, music.artist = %s, music.label = %s, music.release_date = %s, \
        music.asin = %s \
        WHERE music.id= %s AND items.id = music.id", [dictionary['type'], dictionary['title'], dictionary['artist'], \
        dictionary['label'], dictionary['release_date'], dictionary['asin'], item_id])
    if(quantity_diff > 0):
        increase_quantity(quantity_diff, item_type, item_id)
    elif(quantity_diff < 0):
        decrease_quantity(-quantity_diff, item_type, item_id)

def get_cart(client_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clients WHERE user_id = %s", [client_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    cart = row[0]['cart']
    cart = deserialize(cart)
    return cart

def expand_item(item_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE items.id = %s", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    if len(row) == 0:
        return None
    item_type = row[0]['type']
    if item_type == 'book':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM books WHERE books.id = %s", [item_id])
            columns = [col[0] for col in cursor.description]
            book = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
        book[0]['item_type'] = 'book'
        return book[0]
    elif item_type == 'movie':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM movies WHERE movies.id = %s", [item_id])
            columns = [col[0] for col in cursor.description]
            movie = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
        movie[0]['item_type'] = 'movie'
        return movie[0]
    elif item_type == 'magazine':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM magazines WHERE magazines.id = %s", [item_id])
            columns = [col[0] for col in cursor.description]
            magazine = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
        magazine[0]['item_type'] = 'magazine'
        return magazine[0]
    elif item_type == 'music':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM music WHERE music.id = %s", [item_id])
            columns = [col[0] for col in cursor.description]
            music = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
            print(music)
        music[0]['item_type'] = 'music'
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(music)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        return music[0]

def update_cart(client_id, cart, new_id=None):
    cart = serialize(cart)
    curs = connection.cursor()
    curs.execute("UPDATE clients SET clients.cart = %s WHERE clients.user_id = %s", [cart, client_id])
    if (new_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * \
                FROM items \
                WHERE items.id = %s", [new_id])
            columns = [col[0] for col in cursor.description]
            row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
        item = row[0]
        return item['type'].capitalize()

def get_unloaned(item_id):
    print(item_id)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM inventory \
                WHERE inventory.item_id = %s AND inventory.loan_id IS NULL", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    item = row
    print("########################################3")
    print(item)
    print(item_id)
    print("########################################3")
    return item[0]['stock_id']

@contract(client_id=int, stock_id=str, item_type=str, returns=None)
def new_loan(client_id, stock_id, item_type):
    curs = connection.cursor()
    curs.execute("CALL new_loan(%s, %s, %s)",[client_id, stock_id, \
                                                item_type])
    clear_cart(client_id)

def clear_cart(client_id):
    curs = connection.cursor()
    curs.execute("UPDATE clients SET cart = NULL WHERE user_id = %s", [client_id])

def get_active_loans(client_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM loans \
                WHERE client_id = %s AND state_id = 1", [client_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    item = row
    return item

def get_all_loans(filter=None):
    query = 'SELECT loans.id, loans.client_id, loans.stock_id, loans.return_date, loans.lent_date, \
    loans.state_id, items.type FROM loans, inventory, items  WHERE \
    (loans.stock_id = inventory.stock_id OR loans.stock_id IS NULL) AND inventory.item_id = items.id '
    if (bool(filter)):
        query = query + 'AND '
        is_first = True
        if 'client_id' in filter:
            query = query + 'loans.client_id = ' + filter['client_id'] + ' '
            is_first = False
        if 'item_id' in filter:
            if (is_first):
                query = query + 'loans.stock_id LIKE \'' + filter['item_id'] + '%\' '
                is_first = False
            else:
                query = query + 'AND loans.stock_id LIKE \'' + filter['item_id'] + '%\' '
        if 'return_date' in filter:
            if (is_first):
                query = query + 'loans.return_date = \'' + filter['return_date'] + '\' '
                is_first = False
            else:
                query = query + 'AND loans.return_date = \'' + filter['return_date'] + '\' '
        if 'item_type' in filter:
            if (is_first):
                query = query + 'items.type = \'' + filter['item_type'] + '\' '
                is_first = False
            else:
                query = query + 'AND items.type = \'' + filter['item_type'] + '\' '
    query = query + ' GROUP BY loans.id ORDER BY loans.id'
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(query)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')    
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    print(row)
    return row

def get_quantity(item_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM items \
                WHERE id = %s", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    item = row[0]
    quantity = int(item['quantity'])
    return quantity

def get_quantity_available(item_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
                FROM items \
                WHERE id = %s", [item_id])
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    item = row[0]
    quantity = int(item['quantity_available'])
    return quantity

@contract(loan_id='str',returns='None')
def return_item(loan_id):
    curs = connection.cursor()
    curs.execute("CALL return_item(%s)", [loan_id])

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