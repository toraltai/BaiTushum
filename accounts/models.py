from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

            if not email:
                raise ValueError("The given email must be set")
            email = self.normalize_email(email)

            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.create_activation_code()
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


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    tel_number = models.CharField(default='+996 ', max_length=20)
    adress = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code

class SpecUser(CustomUser):
    occupation = models.CharField(max_length=100, choices=[
        ('CreditSpecialist', 'Кредитный специалист'),
        ('Creditadministrator', 'Кредитный администратор')
    ], null=True, blank=True)

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
