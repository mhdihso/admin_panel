from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    class Types(models.TextChoices):
        QUESTION_MAKER = "Question_Maker"
        ADMIN = "Admin"

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
