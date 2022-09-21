from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

OCCUPATION = (
    ('Кредит.спец', 'Кредит.спец'),
    ('Кредит.админ', 'Кредит.админ'),

)


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, occupation,password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email),full_name=full_name,occupation=occupation)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email,password,**extra):
        if password is None:
            raise TypeError('Superusers must have a password.')

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email) )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, )
    email = models.EmailField(db_index=True, unique=True)
    full_name = models.CharField(db_index=True,max_length=406)
    occupation = models.CharField(choices=OCCUPATION, max_length=406)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
