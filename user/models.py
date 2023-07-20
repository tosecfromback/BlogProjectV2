from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password, **extra_fields):
        if not email:
            raise ValueError('Users must hane an email address!')
        # now = timezone.localtime()
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            joined_date = timezone.now(),
            last_login = timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, nickname, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nickname, password,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, max_length=155)
    nickname = models.CharField(unique=True, max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['l']
    
    objects = UserManager()

    def __str__(self):
        return self.nickname