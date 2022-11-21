from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

# from portfolio.apps.info.models import Skill
from portfolio.apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("first name", max_length=150)
    mid_name = models.CharField("middle name", max_length=150)
    last_name = models.CharField("last name", max_length=150)

    is_staff = models.BooleanField("staff status",
                                   default=False,
                                   help_text="Designates whether the user can log into this admin site"
                                   )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
                  "Unselect this instead of deleting accounts."
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    # skills = models.ManyToManyField(Skill, )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def full_name(self):
        """
        Return the first_name, mid_name plus last_name, with a space in between.
        """
        full_name = "%s %s %s" % (self.first_name, self.mid_name, self.last_name)
        return full_name.strip()

    def short_name(self):
        """Return the short name for the user."""
        return self.first_name
