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
