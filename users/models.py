from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
OCCUPATION = (
    ('Кредит.спец', 'Кредит.спец'),
    ('Кредит.админ', 'Кредит.админ'),

)


class UserManager(BaseUserManager):
    def create_spec(self, email, username, full_name, phone_number, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), username=username,
                          full_name=full_name, phone_number=phone_number)
        user.set_password(password)
        user.is_staff = True
        user.save()

        return user

    def create_user(self, email, username, full_name, address, phone_number, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), username=username,
                          full_name=full_name, address=address, phone_number=phone_number)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, **extra):
        if password is None:
            raise TypeError('Superusers must have a password.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    full_name = models.CharField('ФИО', db_index=True, max_length=406)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    #
    # def __str__(self):
    #     if self.occupation:
    #         return self.full_name
    #     else:
    #         return f'Имя клиента: {self.full_name}'

class SpecUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    occupation = models.CharField(choices=OCCUPATION,max_length=69)

class ClientUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address =  models.CharField(max_length=169)
