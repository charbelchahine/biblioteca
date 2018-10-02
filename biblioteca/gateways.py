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

def get_vtk_log():
    print('---------------')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM django_user_log;")
        columns = [col[0] for col in cursor.description]
        row = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    print(row)
    return row

def edit_vtk_log(name):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE django_user_log SET vote_count = vote_count + 1 WHERE user_name = %s;", [name])

