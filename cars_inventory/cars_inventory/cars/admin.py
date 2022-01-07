from django.contrib import admin

from .models import Cars


class CarsAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'description')


admin.site.register(Cars, CarsAdmin)