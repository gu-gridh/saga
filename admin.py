from pydoc import Doc
from django.contrib import admin, sites
from .models import *
from diana.abstract.admin_view import *
from diana.abstract.models import DEFAULT_EXCLUDE, DEFAULT_FIELDS, get_fields
from django.contrib.gis import admin


# Register your models here.
@admin.register(Archive)
class SagaArchiveAdmin(admin.ModelAdmin):
    list_display = get_fields(Archive, exclude=DEFAULT_EXCLUDE+["id"])
    search_fields = ['name', 'name2', 'title', 'parent_name']
    autocomplete_fields = ['parent_name']

@admin.register(ArtForm)
class SagaArtFormAdmin(admin.ModelAdmin):
    list_display = get_fields(ArtForm) 

@admin.register(Role)
class SagaRoleAdmin(admin.ModelAdmin):
    list_display = get_fields(Role) 

@admin.register(Publisher)
class SagaPublisherAdmin(admin.ModelAdmin):
    list_display = get_fields(Publisher) 
    search_fields = ['title']

@admin.register(Series)
class SagaSeriesAdmin(admin.ModelAdmin):
    list_display = get_fields(Series) 
    search_fields = ['title', 'publisher_title']
    autocomplete_fields = ['publisher_title']

@admin.register(Volume)
class SagaVolumeAdmin(admin.ModelAdmin):
    list_display = get_fields(Volume)
    search_fields = ['name', 'title', 'series_name']
    autocomplete_fields = ['series_name'] 

@admin.register(Place)
class SagaPlaceAdmin(admin.ModelAdmin):
    list_display = get_fields(Place) 


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
    search_fields = ['title', 'volume_name']
    autocomplete_fields = ['volume_name', 'publisher_id', 'printer_id', 'archive_id']
    inlines = [
            RelIllustrEditionAdmin,
            RelTextEditionAdmin,
        ]

class SagaIllustrationAdmin(admin.ModelAdmin):
    list_display = get_fields(Illustration, exclude=DEFAULT_EXCLUDE+["id"])
    autocomplete_fields = ['archive_name']
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
    
@admin.register(Work)   
class SagaWorkAdmin(admin.ModelAdmin):
    list_display = get_fields(Work, exclude=DEFAULT_EXCLUDE+["id"])
    search_fields = ['title']


class SagaTextAdmin(admin.ModelAdmin):
    list_display = get_fields(SagaText, exclude=DEFAULT_EXCLUDE+["id"])  
    search_fields = ['archive_name']
    autocomplete_fields = ['archive_name', 'work_id']
    inlines = [
            RelPersonTextAdmin,
            RelTextEditionAdmin
    ]


admin.site.register(Edition, SagaEditionAdmin)
admin.site.register(Illustration, SagaIllustrationAdmin)
admin.site.register(Person, SagaPersonAdmin)
admin.site.register(SagaText, SagaTextAdmin)


# ordering = ["Archives", "Art forms", "Roles", "Publishers", "Series", "Volumes", "Editions",  "Saga texts", "Illustrations", "Persons", "Places" ]


# a = get_apps_order('Saga', ordering)