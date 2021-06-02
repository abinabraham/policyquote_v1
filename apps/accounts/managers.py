from django.contrib.auth.base_user import BaseUserManager
import string    
import random # define the random module  
from datetime import datetime
from uuid import uuid4
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        print("username=========",username)
        if not username:
            eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
            # ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
            username = str(eventid)   
        else: 
            username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)