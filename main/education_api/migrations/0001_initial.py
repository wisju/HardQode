# Generated by Django 5.0.2 on 2024-02-29 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("start_date", models.DateTimeField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="owner",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="title")),
                ("video_url", models.URLField(unique=True, verbose_name="video_url")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="lessons",
                        to="education_api.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "lesson",
                "verbose_name_plural": "lessons",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "min_pupils",
                    models.PositiveIntegerField(default=1, verbose_name="min_pupils"),
                ),
                ("max_pupils", models.PositiveIntegerField(verbose_name="max_pupils")),
                (
                    "pupils",
                    models.ManyToManyField(
                        related_name="group_of_pupils",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="users",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="groups",
                        to="education_api.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
            },
        ),
        migrations.CreateModel(
            name="UserProductAccess",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "check_access",
                    models.BooleanField(default=False, verbose_name="check_access"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="pupil_product",
                        to="education_api.product",
                    ),
                ),
                (
                    "pupil",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="pupil",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
