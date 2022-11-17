from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Дата создания"),)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата изменение"),)

    class Meta:
        abstract = True


JISMONIY_SHAXS = "jismoniy_shaxs"
YURIDIK_SHAXS = "yuridik_shaxs"

YANGI = "yangi"
MODERATSIYADA = "moderatsiyada"
TASDIQLANGAN = "tasdiqlangan"
BEKOR_QILINGAN = "bekor_qilingan"


SPONSOR_TYPE = (
    (JISMONIY_SHAXS, 'jismoniy_shaxs'),
    (YURIDIK_SHAXS, 'yuridik_shaxs'),
)

SPONSOR_STATUS = (
    (YANGI, "yangi"),
    (MODERATSIYADA, "moderatsiyada"),
    (TASDIQLANGAN, "tasdiqlangan"),
    (BEKOR_QILINGAN, "bekor_qilingan"),
)


UZCARD = "uzcard"
HUMO = "humo"
VISA = "visa"

PAYMENT_TYPE = (
    (UZCARD, "uzcard"),
    (HUMO, "humo"),
    (VISA, "visa"),
)


class Sponsor(BaseModel):
    full_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=128, unique=True, db_index=True)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    spent_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    organization = models.CharField(max_length=128, null=True, blank=True)

    type = models.CharField(max_length=50, choices=SPONSOR_TYPE, default=SPONSOR_TYPE[1][1])
    status = models.CharField(max_length=50, choices=SPONSOR_STATUS, default=SPONSOR_STATUS[0][1])
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE, default=PAYMENT_TYPE[0][1])
   
    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        ordering = ('-id',)
        verbose_name = _("Homiy")
        verbose_name_plural = _("Homiylar")


class University(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name = _("Университет")
        verbose_name_plural = _("Университеты")


BAKALAVR = "бакалавр"
MAGISTR = "магистр"


STUDENT_TYPE = (
    (BAKALAVR, "bakalavr"),
    (MAGISTR, "magistr"),
)

class Student(BaseModel):
    full_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)

    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    contract = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    type = models.CharField(max_length=50, choices=STUDENT_TYPE)

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name


    class Meta:
        ordering = ("-id",)
        verbose_name = _("Студент")
        verbose_name_plural = _("СтудентЫ")


class Sponsorship(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sponsors')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"Student {self.student} was sponsored by {self.sponsor}"

    class Meta:
        ordering = ("-id",)
        verbose_name = _("Спонсорство")
        verbose_name_plural = _("Спонсорство")
