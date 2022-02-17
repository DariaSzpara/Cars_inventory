from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from cars.models import Cars
from cars.serializers import CarsSerializer


class CarsViewSet(ReadOnlyModelViewSet):
    queryset = Cars.objects.all() 
    serializer_class = CarsSerializer

class CarsList(APIView):
    """
    List all cars, or create a new cars.
    """
    def get(self, request, format=None):
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()