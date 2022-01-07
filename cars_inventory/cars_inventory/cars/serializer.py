from os import makedev
from rest_framework import serializers

from .models import Cars


class CarsSerializer(serializers.ModelSerializer):
    make = serializers.IntegerField(readonly=True)
    model = serializers.IntegerField(readonly=True)

    class Meta:
        model = Cars
        fields = ('name', 'make', 'model')

    def __new__(cls, *args, **kwargs):
        if args and isinstance(args[0], QuerySet):
              queryset = cls._build_queryset(args[0])
              args = (queryset, ) + args[1:]
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    def _build_queryset(cls, queryset):
         # modify the queryset here
         return queryset.annotate(
             make =
             model = 
            
         )