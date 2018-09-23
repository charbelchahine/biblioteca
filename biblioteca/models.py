from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class cUser(AbstractBaseUser):
    #def __init__(self, dictionary):
     #   for k, v in dictionary.items():
      #      setattr(self, k, v)
      # TODO: Fix this
    def save(self, *args, **kwargs):
        pass
    role_id = models.IntegerField()
    user_id = models.IntegerField(unique=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    address_id = models.IntegerField()
    phone_num = models.IntegerField()
    loan_item_count = models.IntegerField()

    USERNAME_FIELD = 'user_id'
    class Meta:
        managed = False
