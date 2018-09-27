from .models import cUser
from django.db import connection
from collections import namedtuple

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
    dict(zip(columns, row))
    for row in cursor.fetchall()
    ]

def userGateway(username, password):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM auth INNER JOIN clients ON auth.user_id=clients.user_id INNER JOIN has_role ON auth.user_id=has_role.user_id WHERE email=%s",[username])
        row = dictfetchall(cursor)
    print(row)
    print("Password is %s",password)
    if row[0]['password'] != password:
        return None
    else:
        current_user = cUser(row[0])
        return current_user

    # user = cUser.objects.raw("SELECT * FROM auth INNER JOIN clients ON auth.user_id=clients.user_id WHERE email=%s",[username])
    # if (user.password == password):
    #      return user
    # else:
    #     return     None

def addUser(dictionary):
    print(dictionary)
    curs = connection.cursor()
    curs.execute("CALL new_client(%s, %s, %s, %s, %s, %s, %s)",[dictionary['l_name'], dictionary['f_name'], dictionary['email'], int(dictionary['address_id']), int(dictionary['phone_num']), dictionary['password'], int(dictionary['role_id'])])


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

