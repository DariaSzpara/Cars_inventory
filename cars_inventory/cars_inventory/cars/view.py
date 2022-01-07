from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .models import Cars
from .serializers import CarsSerializer


class CarsViewSet(ReadOnlyModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'
