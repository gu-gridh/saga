from pydoc import Doc
from django.contrib import admin
from django.contrib.gis.db import models
from .models import *
import diana.abstract.models
from diana.abstract.models import DEFAULT_EXCLUDE, DEFAULT_FIELDS, get_many_to_many_fields
from django.contrib.gis import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

def get_fields(model: models.Model):

    exclude = DEFAULT_EXCLUDE 
    fields  = [field for field in diana.abstract.models.get_fields(model) if field not in exclude]
    return fields

# Register your models here.
@admin.register(Archive)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Archive) + DEFAULT_FIELDS 

@admin.register(Edition)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Edition) + DEFAULT_FIELDS 

@admin.register(Illustration)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Illustration) + DEFAULT_FIELDS 

@admin.register(Person)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Person) + DEFAULT_FIELDS 

@admin.register(Place)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Place) + DEFAULT_FIELDS 

@admin.register(Publisher)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Publisher) + DEFAULT_FIELDS 

@admin.register(SagaText)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(SagaText) + DEFAULT_FIELDS 

@admin.register(Series)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Series) + DEFAULT_FIELDS 

@admin.register(Volume)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Volume) + DEFAULT_FIELDS 

@admin.register(Role)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(Role) + DEFAULT_FIELDS 

@admin.register(RelIllustrEdition)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(RelIllustrEdition) 
@admin.register(RelPersonIllustration)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(RelPersonIllustration) 

@admin.register(RelPersonText)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(RelPersonText) 

@admin.register(RelTextEdition)
class SagaAdmin(admin.ModelAdmin):
    list_display = get_fields(RelTextEdition)  