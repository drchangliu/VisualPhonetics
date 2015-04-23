from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, gender, user_type, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            is_staff = False,
	    gender=gender,
	    user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, gender, user_type):
        user = self.create_user(
	    email,
            password=password,
	    gender=gender,
	    user_type=user_type,
        )
	user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """
    Custom user class.
    """
   
    GENDER_CHOICES = (
	('M', 'Male'), 
   	('F', 'Female'),
    )

    USER_TYPE = (
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('B', 'Student/Teacher'),
    )

    email = models.EmailField('email address', unique=True, db_index=True)
    is_staff = models.BooleanField('is staff', default=False)
    first_name = models.TextField('first name', default=None, null=True)
    last_name = models.TextField('last name', default=None, null=True)
    avatar = models.ImageField('profile picture', upload_to='staticfiles/media/images/avatars/', default="static/media/images/blank-user.jpg", null=True, blank=True)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES)
    user_type = models.CharField('user type', max_length=1, choices=USER_TYPE)

    objects = MyUserManager()

    REQUIRED_FIELDS = ['date_of_birth', 'gender', 'user_type']

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_email(self):
	return self.email

    def get_gender(self):
	return self.gender

    def get_short_name(self):
        if(self.first_name):
            return self.first_name
	return self.email

    def set_avatar(self):
	self.has_picture = True

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_staff:
            return True

        return _user_has_module_perms(self, app_label)
