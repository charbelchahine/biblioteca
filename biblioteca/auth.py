from .models import cUser
from django.conf import settings
from django.db import connection
from collections import namedtuple
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

class auth:
        
    def authenticate(self, request, username=None, password=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT *\
FROM clients LEFT JOIN (SELECT users.id, has_role.role_id, auth.password, roles.name\
                FROM users, has_role, auth, roles\
                where has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id) as sq1 ON (sq1.id = clients.user_id)\
WHERE clients.email = %s;",[username]) # Thank you Matt for this amazing query
            columns = [col[0] for col in cursor.description]
            row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

        print(row)
        print("Password is %s",password)
        if(password is not None):
            if len(row) is 0 or row[0]['password'] != password:
                return None
            else:
                current_user = cUser(row[0])
                return current_user

    def get_user(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT *\
FROM clients LEFT JOIN (SELECT users.id, has_role.role_id, auth.password, roles.name\
                FROM users, has_role, auth, roles\
                where has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id) as sq1 ON (sq1.id = clients.user_id)\
WHERE sq1.id = %s;",[user_id])
            columns = [col[0] for col in cursor.description]
            row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]
        print(row[0])
        return cUser(row[0])


def authorize_admin(request): # imrpove this - use django's built in auth check instead
    if(not request.user.is_authenticated or request.user.role_id is not 1):
        return False
    else:
        return True