from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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
    address_id = models.IntegerField()
    phone_num = models.IntegerField()
    loan_item_count = models.IntegerField()
    id = models.IntegerField(unique = True, primary_key = True)

    def __init__(self, dictionary, *args, **kwargs):
        self.role_id = int(dictionary['role_id'])
        self.user_id = dictionary['user_id']
        self.email = dictionary['email']
        self.password = dictionary['password']
        self.f_name = dictionary['f_name']
        self.l_name = dictionary['l_name']
        self.address_id = dictionary['address_id']
        self.phone_num = dictionary['phone_num']
        self.loan_item_count = dictionary['loan_item_count']
        self.id = self.user_id

    USERNAME_FIELD = 'id'
    class Meta:
        managed = False
