from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.student = False
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.BigAutoField(
        primary_key=True,
    )

    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
        validators=[
            validators.EmailValidator("Invalid Email")
        ]
    )
    
    first_name = models.CharField(
        max_length=50, 
        verbose_name='First Name',
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(3, message="First name is too short"),
            validators.MaxLengthValidator(15, message="First name is too long"),
        ]
    )

    last_name = models.CharField(
        max_length=50, 
        verbose_name='Last Name',
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(3, message="Last name is too short"),
            validators.MaxLengthValidator(15, message="Last name is too long"),
        ]
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    merchant=models.BooleanField(default=False)
    customer = models.BooleanField(default=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    @property
    def is_merchant(self):
        "Is the user a student?"
        return self.merchant
    
    @property
    def is_customer(self):
        "Is the user an instructor?"
        return self.customer

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class CustomerDetails(models.Model):
    STATES = (
        ('Kerala', 'Kerala'),
        ('Karnataka', 'Karnataka')
    )

    id = models.BigAutoField(
        primary_key=True,
    )

    address = models.TextField(
        verbose_name="Address",
        max_length=300,
        validators=[
            validators.MinLengthValidator(10, "Address is too short")
        ]
    )

    pin = models.CharField(
        verbose_name="Postal Code",
        max_length=6,
        validators=[
            validators.RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$', "Invalid Pin Number")
        ]
    )

    city = models.CharField(
        verbose_name="City",
        max_length=50,
        validators=[
            validators.MinLengthValidator(3, "Invalid city name")
        ]
    )

    state = models.CharField(
        max_length=50,
        choices=STATES,
        default='Kerala'
    )

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )