from .models import cUser
from django.conf import settings
from django.db import connection
from collections import namedtuple

class auth:
        
    def authenticate(self, request, username=None, password=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT *\
FROM clients LEFT JOIN (SELECT users.id, has_role.role_id, auth.password, roles.name\
                FROM users, has_role, auth, roles\
                where has_role.user_id = users.id AND users.id = auth.user_id AND roles.id = has_role.role_id) as sq1 ON (sq1.id = clients.user_id)\
WHERE sq1.name = %s;",[username]) # Thank you Matt for this amazing query
            columns = [col[0] for col in cursor.description]
            row = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

        print(row)
        print("Password is %s",password)
        if(password is not None):
            if row[0]['password'] != password:
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