from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3


class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'type', 'year']


class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]


# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
