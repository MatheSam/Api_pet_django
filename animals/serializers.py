from rest_framework import serializers
from animals.exceptions import NonUpdatableKeyErros
from groups.models import Group
from groups.serializers import GroupSerializer
from traits.models import Trait
import ipdb
from traits.serializers import TraitSerializer
from .models import Animal, Sex
from math import log


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    sex = serializers.ChoiceField(
        choices=Sex.choices,
        default=Sex.OTHER,
    )

    traits = TraitSerializer(many=True)
    group = GroupSerializer()

    age_in_human_years = serializers.SerializerMethodField(method_name='obtain_age')

    def create(self, validated_data: dict) -> Animal:
        group_data = validated_data.pop("group")
        traits_data = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group_data)

        animal_obj = Animal.objects.create(**validated_data, group=group)

        for trait in traits_data:
            trait, _ = Trait.objects.get_or_create(**trait)
            animal_obj.traits.add(trait)

        return animal_obj

    def update(self, instance: Animal, validated_data: dict) -> Animal:
        for key, value in validated_data.items():
            if key == 'sex' or key == 'group' or key == 'traits':
                msg = {key: f'You can not update {key} property.'}
                raise NonUpdatableKeyErros(msg)
            setattr(instance, key, value)

        instance.save()

        return instance

    def obtain_age(self, obj: Animal):
        return obj.convert_dog_age_to_human_years()
