# Generated by Django 4.2.4 on 2024-05-31 09:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                    "image",
                    models.FileField(
                        upload_to="images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=("png", "jpg", "jpeg")
                            )
                        ],
                        verbose_name="Images",
                    ),
                ),
                (
                    "category_by_user",
                    models.CharField(
                        choices=[
                            ("Cat", "Cat"),
                            ("Dog", "Dog"),
                            ("Car", "Car"),
                            ("Plane", "Plane"),
                            ("Bird", "Bird"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "category_by_ai",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Cat", "Cat"),
                            ("Dog", "Dog"),
                            ("Car", "Car"),
                            ("Plane", "Plane"),
                            ("Bird", "Bird"),
                        ],
                        max_length=32,
                    ),
                ),
            ],
        ),
    ]
