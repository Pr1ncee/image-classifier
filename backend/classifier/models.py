from django.core.validators import FileExtensionValidator
from django.db import models

from classifier.enums.category_enum import CategoryEnum
from image_classifier.config import general_config


class Image(models.Model):
    image = models.FileField(
        upload_to=general_config.TARGET_IMAGE_DIR,
        verbose_name="Images",
        validators=[FileExtensionValidator(allowed_extensions=("png", "jpg", "jpeg"))],
    )
    category_by_user = models.CharField(max_length=32, choices=CategoryEnum.choices)
    category_by_ai = models.CharField(
        max_length=32, choices=CategoryEnum.choices, blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.category_by_user}"
