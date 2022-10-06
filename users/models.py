from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

OCCUPATION = (
    ('Кредит.спец', 'Кредит.спец'),
    ('Кредит.админ', 'Кредит.админ'),

)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # def __str__(self):
    #     if self.occupation:
    #         return self.full_name
    #     else:
    #         return f'Имя клиента: {self.full_name}'


class SpecUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # full_name = models.CharField(max_length=100, verbose_name='ФИО')
    # occupation = models.CharField(choices=OCCUPATION, max_length=69)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=169)
