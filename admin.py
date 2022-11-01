from pydoc import Doc
from django.contrib import admin
from django.contrib.gis.db import models
from .models import *
import diana.abstract.models
from diana.abstract.models import DEFAULT_EXCLUDE, DEFAULT_FIELDS, get_fields
from django.contrib.gis import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Archive)
class SagaArchiveAdmin(admin.ModelAdmin):
    list_display = get_fields(Archive, exclude=DEFAULT_EXCLUDE+["id"])

@admin.register(Place)
class SagaPlaceAdmin(admin.ModelAdmin):
    list_display = get_fields(Place) 

@admin.register(Publisher)
class SagaPublisherAdmin(admin.ModelAdmin):
    list_display = get_fields(Publisher) 

@admin.register(Series)
class SagaSeriesAdmin(admin.ModelAdmin):
    list_display = get_fields(Series) 

@admin.register(Volume)
class SagaVolumeAdmin(admin.ModelAdmin):
    list_display = get_fields(Volume) 

@admin.register(Role)
class SagaRoleAdmin(admin.ModelAdmin):
    list_display = get_fields(Role) 


class RelIllustrEditionAdmin(admin.TabularInline):
    model = RelIllustrEdition
    extra = 1

class RelPersonIllustrationAdmin(admin.TabularInline):
    model = RelPersonIllustration
    extra = 1

class RelPersonTextAdmin(admin.TabularInline):
    model = RelPersonText
    extra = 1

class RelTextEditionAdmin(admin.TabularInline):
    model = RelTextEdition
    extra = 1
   

class SagaEditionAdmin(admin.ModelAdmin):
    list_display = get_fields(Edition, exclude=DEFAULT_EXCLUDE+["id"]) 
    inlines = [
            RelIllustrEditionAdmin,
            RelTextEditionAdmin,
        ]

class SagaIllustrationAdmin(admin.ModelAdmin):
    list_display = get_fields(Illustration, exclude=DEFAULT_EXCLUDE+["id"])
    inlines =  [
        RelIllustrEditionAdmin,
        RelPersonIllustrationAdmin,
        ]

class SagaPersonAdmin(admin.ModelAdmin):
    list_display = get_fields(Person, exclude=DEFAULT_EXCLUDE+["id"])  
    inlines = [
            RelPersonIllustrationAdmin, 
            RelPersonTextAdmin,
            ]

class SagaTextAdmin(admin.ModelAdmin):
    list_display = get_fields(SagaText, exclude=DEFAULT_EXCLUDE+["id"])  
    inlines = [
            RelPersonTextAdmin,
            RelTextEditionAdmin
    ]


admin.site.register(Edition, SagaEditionAdmin)
admin.site.register(Illustration, SagaIllustrationAdmin)
admin.site.register(Person, SagaPersonAdmin)
admin.site.register(SagaText, SagaTextAdmin)