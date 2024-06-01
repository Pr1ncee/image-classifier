from django.db import models


class CategoryEnum(models.TextChoices):
    CAT = "Cat"
    DOG = "Dog"
    CAR = "Car"
    PLANE = "Plane"
    BIRD = "Bird"

    @classmethod
    def get_list_values(cls):
        return [choice[1] for choice in cls.choices]
