from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2  # Number of empty CarModel forms

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make', 'dealer_id')
    list_filter = ('car_make', 'type', 'year')

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

