from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalsView(APIView):
    def get(self, request):
        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class AnimalDetailView(APIView):
    def get(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serializer = AnimalSerializer(animal)

        return Response(serializer.data)

    def patch(sel, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)

        serializer = AnimalSerializer(animal, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, animal_id: int) -> Response:
        user = get_object_or_404(Animal, id=animal_id)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)