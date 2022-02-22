"""from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, name, firstName, pseudo, email, password=None, **kwargs):
        Create and return a `User` with an email, phone number, username and password.
        if name is None:
            raise TypeError('Le nom est incorrecte.')
        if firstName is None:
            raise TypeError('Le pre-nom est incorrecte.')
        if pseudo is None:
            raise TypeError('Le pseudo est incorrecte.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(name=name, firstName=firstName, pseudo=pseudo, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, firstName, pseudo, email, password):
        Create and return a `User` with superuser (admin) permissions.
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if name is None:
            raise TypeError('Le nom pour le superusers est incorrecte.')
        if firstName is None:
            raise TypeError('Le pre-nom pour le superusers est incorrecte.')
        if pseudo is None:
            raise TypeError('Le pseudo pour le superusers est incorrecte.')

        user = self.create_user(name, firstName, pseudo, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(db_index=True, max_length=255, unique=True)
    firstName = models.CharField(db_index=True, max_length=255, unique=True)
    pseudo = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'firstName', 'pseudo']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
        """