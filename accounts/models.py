from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, full_name=None, first_name=None,
                     last_name=None, is_staff=False, is_admin=False,
                     is_superuser=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an Email Address')

        if not password:
            raise ValueError('Users must have a Password')

        if not full_name:
            raise ValueError('Users must provide Full Name')

        '''This is how you create a user in Django'''
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            #first_name=first_name,
            #last_name=last_name,
        )
        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None, full_name=None, first_name=None,
                         last_name=None, is_staff=False, is_admin=False,
                         is_superuser=False):
        user = self._create_user(
                email,
                full_name=full_name,
                #first_name=first_name,
                #last_name=last_name,
                password=password,
                is_staff=True,
                is_admin=False,
                is_superuser=False,
        )
        return user

    def create_adminuser(self, email, password=None, full_name=None, first_name=None,
                         last_name=None, is_staff=False, is_admin=False,
                         is_superuser=False):
        user = self._create_user(
                email,
                full_name=full_name,
                #first_name=first_name,
                #last_name=last_name,
                password=password,
                is_staff=True,
                is_admin=True,
                is_superuser=False,
        )
        return user

    def create_superuser(self, email, password=None, full_name=None, first_name=None,
                         last_name=None, is_staff=False, is_admin=False,
                         is_superuser=False):
        user = self._create_user(
                email,
                full_name=full_name,
                #first_name=first_name,
                #last_name=last_name,
                password=password,
                is_staff=True,
                is_admin=True,
                is_superuser=True,
        )
        return user

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(_('Username'), max_length=30, blank=True)
    email = models.EmailField(_('Your Email Address'), unique=True)
    full_name = models.CharField(_('Full Name'), max_length=30, blank=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_admin = models.BooleanField(_('Admin'), default=False)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True) #meaning user can log in our project
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name'] #['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''Returns the first_name plus the last_name,
        with a space in between.'''
        return self.email
        # full_name = '%s %s' % (self.first_name, self.last_name)
        # return full_name.strip()

    def get_short_name(self):
        '''Returns the short name for the user.'''
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''Sends an email to this User.'''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        '''Simplest possible answer: Yes, always'''
        return True

