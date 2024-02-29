from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.


class Product(models.Model):
    """Модель Product для сущности продукта"""

    name = models.CharField(max_length=64, null=False, blank=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        verbose_name="owner",
        to_field="id",
        related_name="owner",
    )
    start_date = models.DateTimeField(null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class UserProductAccess(models.Model):
    """Модель UserProductAccess для определения доступа пользователя к продукту"""

    pupil = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="pupil")
    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, related_name="pupil_product"
    )

    check_access = models.BooleanField(default=False, verbose_name="check_access")


class Lesson(models.Model):
    """Модель Lesson для сущности урока"""

    title = models.CharField(
        max_length=128, null=False, blank=False, verbose_name="title"
    )
    video_url = models.URLField(
        unique=True, null=False, blank=False, verbose_name="video_url"
    )

    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, related_name="lessons"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = "lessons"


class Group(models.Model):
    """Модель Group для сущности группы пользователей"""

    name = models.CharField(
        max_length=128, null=False, blank=False, verbose_name="name"
    )
    min_pupils = models.PositiveIntegerField(
        verbose_name="min_pupils", default=1, null=False, blank=False
    )
    max_pupils = models.PositiveIntegerField(
        verbose_name="max_pupils", null=False, blank=False
    )

    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, related_name="groups"
    )
    pupils = models.ManyToManyField(
        User, verbose_name="users", related_name="group_of_pupils"
    )

    def __str__(self):
        return f"{self.product.name}: {self.name}"

    def clean(self):
        super().clean()

        if self.pk is not None:
            pupils_amount = self.pupils.count()
            max_students = self.max_pupils

            if pupils_amount > max_students:
                raise ValidationError(f"A large number of students")

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"
