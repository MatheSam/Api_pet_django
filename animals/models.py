from enum import unique
from unicodedata import decimal
from django.db import models
import math


class Sex(models.TextChoices):
    MALE = "Macho"
    FEMALE = "Femea"
    OTHER = "Não informado"


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    sex = models.CharField(max_length=15, choices=Sex.choices, default=Sex.OTHER)

    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="animals",
    )

    traits = models.ManyToManyField("traits.Trait", related_name="animals")

    def convert_dog_age_to_human_years(self):
        human_age = round((16 * math.log(self.age)) + 31, 2)
        return human_age