from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    """ """

    def create_user(self, email, password=None, **extra_fields):
        """ """
        if not email:
            raise ValueError('email address invalid')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255)
    number_of_dependents = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    investment_experience = models.CharField(max_length=255)
    employer_name = models.CharField(max_length=255)
    trade_options = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=255)
    strategy = models.CharField(max_length=255)
    term_period = models.CharField(max_length=255)
    fund1 = models.CharField(max_length=255)
    fund1_percentage = models.CharField(max_length=255)
    fund1_prospectus = models.CharField(max_length=255)
    fund2 = models.CharField(max_length=255)
    fund2_percentage = models.CharField(max_length=255)
    fund2_prospectus = models.CharField(max_length=255)
    fund3 = models.CharField(max_length=255)
    fund3_percentage = models.CharField(max_length=255)
    fund3_prospectus = models.CharField(max_length=255)
    cash = models.CharField(max_length=255)
    cash_percentage = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
