from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import diana.abstract.models as abstract
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Archive(abstract.AbstractBaseModel):
    LEVEL_CHOICE = (
        ('A', 'Avdelning'),
        ('S', 'Serie'),
        ('V', 'Volym'),
        ('O', 'Omslag'),
        ('U', 'Underserie 1'),
        ('U2', 'Underserie 2')

    )
    archive_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    notes = models.TextField(blank=True)
    level = models.CharField(max_length=255, choices=LEVEL_CHOICE, null=True)
    parent_id = models.ForeignKey('Archive', on_delete=models.PROTECT, null=True)

    class Meta:
        # managed = False
        db_table = 'archive'


class Edition(abstract.AbstractBaseModel):

    edition_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    preface = models.TextField(blank=True)
    backtext = models.TextField(blank=True)
    paratext = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    num = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    libris = models.CharField(max_length=255, null=True)
    volume_id = models.ForeignKey('Archive', on_delete=models.PROTECT, null=True)

    class Meta:
        # managed = False
        db_table = 'edition'


class Illustration(abstract.AbstractBaseModel):
    illustration_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    method = models.CharField(max_length=255, null=True)
    colour = models.SmallIntegerField(null=True)
    filename = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    archive_id = models.ForeignKey('Archive', on_delete=models.PROTECT, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'illustration'


class Person(abstract.AbstractBaseModel):
    SEX_CHOICE = (
        ('M', 'Man'),
        ('K', 'Kvinna')
    )
    person_id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=255, null=True)
    maidenname = models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, choices=SEX_CHOICE)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    birthplace = models.CharField(max_length=255, null=True)
    deathplace = models.CharField(max_length=255, null=True)
    wikidata = models.CharField(max_length=255, null=True)
    librisxl = models.CharField(max_length=255, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'person'


class Place(abstract.AbstractBaseModel):
    place_id = models.AutoField(primary_key=True)
    placename = models.CharField(max_length=255, null=True)
    geom = models.MultiPolygonField(null=True)
    wikidata = models.CharField(max_length=255, null=True)
    parish_id = models.IntegerField(null=True)
    municipality_id = models.IntegerField(null=True)
    notes = models.TextField(blank=True)


    class Meta:
        db_table = 'place'

class Publisher(abstract.AbstractBaseModel):
    SEX_CHOICE = (
        ('M', 'Man'),
        ('K', 'Kvinna')
    )
    publisher_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255, null=True)
    notes = models.TextField(blank=True)
    startyear = models.IntegerField(null=True)
    endyear = models.IntegerField(null=True)

    class Meta:
        db_table = 'publisher'


class SagaText(abstract.AbstractBaseModel):
    VARIANT_CHOICE = (
        ('T', 'Tryckt'),
        ('M', 'Manus 1'),
        ('M2', 'Manus 2'),
        ('M3', 'Manus 3'),

    )
    sagatext_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    originaltitle = models.CharField(max_length=255, null=True)
    langiso = models.CharField(max_length=4, null=True)
    variant = models.CharField(max_length=255, choices=VARIANT_CHOICE, null=True)
    filename = models.CharField(max_length=255, null=True)
    pages = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    archive_id = models.ForeignKey('Archive', on_delete=models.PROTECT, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'sagatext'

class Series(abstract.AbstractBaseModel):
    series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    publisher_id = models.ForeignKey('Publisher', on_delete=models.PROTECT, null=True)
    notes = models.TextField(blank=True)
    startyear = models.IntegerField(null=True)
    endyear = models.IntegerField(null=True)

    class Meta:
        db_table = 'series'


class Volume(abstract.AbstractBaseModel):
    volume_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    year = models.IntegerField(null=True)
    isbn = models.CharField(max_length=255, null=True)
    libris = models.CharField(max_length=255, null=True)
    litteraturbanken = models.CharField(max_length=255, null=True)
    series_id = models.ForeignKey('Series', on_delete=models.PROTECT, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'volume'


class Role(abstract.AbstractBaseModel):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'role'

# Do we need AbstractBaseModel or simple model?     
class RelIllustrEdition(models.Model):
    rel_illustr_edition_id = models.AutoField(primary_key=True)
    illustration_id = models.ForeignKey('Illustration', on_delete=models.PROTECT, null=True)
    edition_id = models.ForeignKey('Edition', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'rel_illustr_edition'


class RelPersonIllustration(models.Model):
    rel_illustr_edition_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person', on_delete=models.PROTECT, null=True)
    illustration_id = models.ForeignKey('Illustration', on_delete=models.PROTECT, null=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)


    class Meta:
        db_table = 'rel_person_illustr'

class RelPersonText(models.Model):
    rel_person_text_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person', on_delete=models.PROTECT, null=True)
    sagatext_id = models.ForeignKey('SagaText', on_delete=models.PROTECT, null=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'rel_person_text'

class RelTextEdition(models.Model):
    rel_text_edition_id = models.AutoField(primary_key=True)
    sagatext_id = models.ForeignKey('SagaText', on_delete=models.PROTECT, null=True)
    edition_id = models.ForeignKey('Edition', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'rel_text_edition'