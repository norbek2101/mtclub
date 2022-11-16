from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=256, verbose_name=_("ФИО"),)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Дата создания"),)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата изменение"),)

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
