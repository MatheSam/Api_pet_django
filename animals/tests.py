from django.test import TestCase
from animals.models import Animal

from groups.models import Group
from traits.models import Trait
import ipdb


# Create your tests here.
class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.animal_data = {
            "name": "Beethoven",
            "age": 1,
            "weight": 30,
            "sex": "Macho",
            "group": {"name": "cão", "scientific_name": "canis familiaris"},
            "traits": [{"name": "peludo"}, {"name": "médio porte"}],
        }

        cls.group_data = cls.animal_data.pop("group")
        cls.traits_data = cls.animal_data.pop("traits")

        cls.group = Group.objects.create(**cls.group_data)

        cls.animal = Animal.objects.create(**cls.animal_data, group=cls.group)

        for trait in cls.traits_data:
            actual_trait, _ = Trait.objects.get_or_create(**trait)
            cls.animal.traits.add(actual_trait)

    def test_animal_field_attributes(self):
        name = self.animal._meta.get_field('name').max_length
        weight_digits = self.animal._meta.get_field('weight').max_digits
        weight_decimal = self.animal._meta.get_field('weight').decimal_places
        sex = self.animal._meta.get_field('sex').max_length

        self.assertEqual(name, 50)
        self.assertEqual(weight_digits, 10)
        self.assertEqual(weight_decimal, 2)
        self.assertEqual(sex, 15)

    def test_convert_dog_age(self):
        to_human_age = self.animal.convert_dog_age_to_human_years()

        self.assertEqual(to_human_age, 31)

    def test_animal_fields(self):
        self.assertEqual(self.animal.name, self.animal_data['name'])
        self.assertEqual(self.animal.age, self.animal_data['age'])
        self.assertEqual(self.animal.weight, self.animal_data['weight'])
        self.assertEqual(self.animal.sex, self.animal_data['sex'])
        self.assertEqual(self.animal.name, self.animal_data['name'])
    

