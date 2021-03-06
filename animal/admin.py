from codecs import getencoder
from django.contrib import admin
from .models import (
   Animal,
   Breed,
   Color,
   TypeAnimal, 
)
# Register your models here.

class AnimalShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date')
    list_filter =  ('id', 'name', 'birth_date')
    search_fields = ('name', )

class BreedShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed', 'fk_type_animal')
    list_filter =  ('fk_type_animal', )
    search_fields = ('breed', )

class ColorShowAdmin(admin.ModelAdmin):
    list_display = ('color',)
    search_fields = ('color',)

class TypeAnimalShowAdmin(admin.ModelAdmin):
    list_display = ('type_animal',)
    search_fields = ('type_animal',)

admin.site.register(Animal, AnimalShowAdmin)
admin.site.register(Breed, BreedShowAdmin)
admin.site.register(Color, ColorShowAdmin)
admin.site.register(TypeAnimal, TypeAnimalShowAdmin)

