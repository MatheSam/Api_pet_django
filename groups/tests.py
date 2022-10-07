from django.test import TestCase
from animals.models import Animal

from groups.models import Group
from traits.models import Trait
import ipdb


# Create your tests here.
class GroupsModelTest(TestCase):
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

    def test_groups_field_attributes(self):
        name = self.group._meta.get_field('name').max_length
        scientific_name = self.group._meta.get_field('scientific_name').max_length

        self.assertEqual(name, 20)
        self.assertEqual(scientific_name, 50)

    def test_groups_fields(self):
        self.assertEqual(self.group.name, self.group_data['name'])
        self.assertEqual(self.group.scientific_name, self.group_data['scientific_name'])
