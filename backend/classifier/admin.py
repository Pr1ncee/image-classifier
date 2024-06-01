from django.contrib import admin

from classifier.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
