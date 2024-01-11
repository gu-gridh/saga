from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import diana.abstract.models as abstract
from diana.abstract.mixins import GenderedMixin
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Archive(abstract.AbstractBaseModel):
    LEVEL_CHOICE = (
        ('A', 'Avdelning'),
        ('S', 'Serie'),
        ('V', 'Volym'),
        ('O', 'Omslag'),
        ('U1', 'Underserie 1'),
        ('U2', 'Underserie 2')
    )

    name = models.CharField(max_length=255, verbose_name= _("digital arkivbeteckning"), null=True, blank=True)
    name2 = models.CharField(max_length=255, verbose_name= _("analog arkivbeteckning"), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name= _("beskrivning"), null=True, blank=True)
    level = models.CharField(max_length=4, choices=LEVEL_CHOICE, verbose_name= _("nivå"), null=True, blank=True)
    parent_name = models.ForeignKey('Archive', on_delete=models.PROTECT, verbose_name= _("överordnad nivå"), null=True, blank=True)
    notes = models.TextField(verbose_name= _("innehåll"), null=True, blank=True)
    notes2 = models.TextField(verbose_name= _("anteckningar"), null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("arkiv")
        verbose_name_plural = _("arkiv")


class ArtForm(abstract.AbstractBaseModel):
    formname = models.CharField(max_length=255, verbose_name= _("teknik"), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name= _("beskrivning"), null=True, blank=True)
    
    def __str__(self):
        return f"{self.formname}"

    class Meta:
        verbose_name = _("konstnärlig teknik")
        verbose_name_plural = _("konstnärliga tekniker")

class MakeForm(abstract.AbstractBaseModel):
    make_name = models.CharField(max_length=255, verbose_name= _("utförande"), null=True, blank=True)
    
    def __str__(self):
        return f"{self.make_name}"

    class Meta:
        verbose_name = _("utförande")
        verbose_name_plural = _("utförande")

class Role(abstract.AbstractBaseModel):
    role_name = models.CharField(verbose_name= _("roll"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.role_name}"

    class Meta:
        verbose_name = _("roll för person")
        verbose_name_plural = _("roller för person")

    
class Publisher(abstract.AbstractBaseModel):

    title = models.CharField(max_length=255, verbose_name= _("Organisation"), blank=True, null=True)
    place = models.CharField(max_length=255, verbose_name= _("Ort"), blank=True, null=True)
    startyear = models.IntegerField(verbose_name= _("Startår"), blank=True, null=True)
    endyear = models.IntegerField(verbose_name= _("Slutår"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Anteckningar"), blank=True, null=True)
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("organisation")
        verbose_name_plural = _("organisationer")


class Series(abstract.AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name= _("name"), blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name= _("titel"), blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name= _("undertitel"), blank=True, null=True)
    publisher_title = models.ForeignKey(Publisher, verbose_name= _("förlag"), on_delete=models.PROTECT, blank=True, null=True)
    startyear = models.IntegerField(verbose_name= _("startår"), blank=True, null=True)
    endyear = models.IntegerField(verbose_name= _("slutår"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("publikationsserie")
        verbose_name_plural = _("publikationsserier")


class Volume(abstract.AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name= _("volymnummer"), blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name= _("titel"), blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name= _("undertitel"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("utgivningsår"), blank=True, null=True)
    isbn = models.CharField(max_length=255, verbose_name= _("isbn"), blank=True, null=True)
    libris = models.CharField(max_length=255, verbose_name= _("libris"), blank=True, null=True)
    litteraturbanken = models.CharField(max_length=255, verbose_name= _("Litteraturbanken"), blank=True, null=True)
    series_name = models.ForeignKey(Series, on_delete=models.PROTECT, verbose_name= _("publikationsserie"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Sagas stora katalog"), blank=True, null=True)
    notes2 = models.TextField(verbose_name= _("anteckningar"), blank=True, null=True)
    notes3 = models.TextField(verbose_name= _("interna anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("publikationsvolym")
        verbose_name_plural = _("publikationsvolymer")


class Edition(abstract.AbstractBaseModel):

    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    preface = models.TextField(blank=True, verbose_name= _("pre-face"), null=True)
    backtext = models.TextField(verbose_name= _("back text"), blank=True, null=True)
    paratext = models.TextField(verbose_name= _("para text"), blank=True, null=True)
    num = models.IntegerField(verbose_name= _("num"), blank=True, null=True)
    pages = models.IntegerField(verbose_name= _("pages"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    libris = models.CharField(max_length=255, verbose_name= _("libris"), blank=True, null=True)
    volume_name = models.ForeignKey('Volume', on_delete=models.PROTECT, verbose_name= _("volume name"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

class Edition(abstract.AbstractBaseModel):
    REVISION_CHOICE = (
        ('M', 'Obetydliga revideringar'),
        ('S', 'Små revideringar'),
        ('L', 'Stora revideringar')
    )
    title = models.CharField(max_length=255, verbose_name= _("Titel"), blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name= _("Undertitel"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("Utgivningsår"), blank=True, null=True)
    volume_name = models.ForeignKey('Volume', on_delete=models.PROTECT, verbose_name= _("Publikationsserienr"), blank=True, null=True)
    version = models.IntegerField(verbose_name= _("Upplaga"), blank=True, null=True)
    make_id = models.ForeignKey(MakeForm, on_delete=models.PROTECT, verbose_name= _("Utförande"), blank=True, null=True) 
    preface = models.TextField(blank=True, verbose_name= _("Text titelsida"), null=True)
    backtext = models.TextField(verbose_name= _("Text baksida"), blank=True, null=True)
    paratext = models.TextField(verbose_name= _("para text"), blank=True, null=True)
    num = models.IntegerField(verbose_name= _("num"), blank=True, null=True)
    publisher_id = models.ForeignKey(Publisher, verbose_name= _("Utgivare"), related_name= 'saga_publisher_id', on_delete=models.PROTECT, blank=True, null=True)
    printer_id = models.ForeignKey(Publisher, verbose_name= _("Tryckeri"), related_name= 'saga_printer_id', on_delete=models.PROTECT, blank=True, null=True)
    pages = models.IntegerField(verbose_name= _("Antal sidor"), blank=True, null=True)
    height = models.IntegerField(verbose_name= _("Format höjd (mm)"), blank=True, null=True)
    width = models.IntegerField(verbose_name= _("Format breddn (mm)"), blank=True, null=True)
    isbn = models.CharField(max_length=255, verbose_name= _("ISBN"), blank=True, null=True)
    libris = models.CharField(max_length=255, verbose_name= _("Libris"), blank=True, null=True)
    printnr = models.CharField(max_length=255, verbose_name= _("antal tryckta ex"), blank=True, null=True)
    archive_id = models.ForeignKey(Archive, on_delete=models.PROTECT, verbose_name= _("Arkivexemplar"), null=True, blank=True)
    revisions = models.CharField(max_length=4, choices=REVISION_CHOICE, verbose_name= _("Ändringar"), null=True, blank=True)
    notes = models.TextField(verbose_name= _("Anteckningar ändringar"), blank=True, null=True)
    editorial = models.TextField(verbose_name= _("Redaktionell text"), blank=True, null=True)
    edit_notes = models.TextField(verbose_name= _("Anteckningar red. text"), blank=True, null=True)
    general_notes = models.TextField(verbose_name= _("Generella anteckningar"), blank=True, null=True)
    internal_notes = models.TextField(verbose_name= _("Interna anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Upplaga")
        verbose_name_plural = _("Upplagor")

class Work(abstract.AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name= _("titel"), blank=True, null=True)
    author_id = models.ForeignKey(Series, on_delete=models.PROTECT, verbose_name= _("Författare"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Interna anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Verk")
        verbose_name_plural = _("Verk")

class SagaText(abstract.AbstractBaseModel):
    VARIANT_CHOICE = (
        ('T', 'Tryckt'),
        ('M', 'Manus 1'),
        ('M2', 'Manus 2'),
        ('M3', 'Manus 3'),
    )
    title = models.CharField(max_length=255, verbose_name= _("Titel"), blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name= _("Undertitel"), blank=True, null=True)
    originaltitle = models.CharField(max_length=255, verbose_name= _("Originaltitel"), blank=True, null=True)
    langiso = models.CharField(max_length=4, verbose_name= _("Språk ISO"), blank=True, null=True)
    variant = models.CharField(max_length=255, choices=VARIANT_CHOICE, verbose_name= _("variant"), blank=True, null=True)
    filename = models.CharField(max_length=255, verbose_name= _("file name"), blank=True, null=True)
    startpage = models.IntegerField(verbose_name= _("Startsida"), blank=True, null=True)
    endpage = models.IntegerField(verbose_name= _("Slutsida"), blank=True, null=True)
    archive_name = models.ForeignKey(Archive, verbose_name= _("Arkiv-ID"), on_delete=models.PROTECT, blank=True, null=True)
    notes = models.TextField(verbose_name= _("Anteckningar"), blank=True, null=True)
    internal_notes = models.TextField(verbose_name= _("Interna anteckningar"), blank=True, null=True)
    num_images = models.IntegerField(verbose_name= _("Antal illustrationer"), blank=True, null=True)
    image_notes = models.TextField(verbose_name= _("Anteckningar för illustrationer"), blank=True, null=True)
    edition_id = models.ForeignKey(Edition, verbose_name= _("Upplaga"), on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Tryckt text")
        verbose_name_plural = _("Tryckta texter")

class Illustration(abstract.AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name= _("titel"), blank=True, null=True)
    method = models.ForeignKey(ArtForm, on_delete=models.PROTECT, verbose_name= _("Konstnärlig teknik"), blank=True, null=True)
    colour = models.BooleanField(verbose_name= _("Färg, ja)"),blank=True, null=True)
    # filename = models.CharField(max_length=255,verbose_name= _("file name"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    archive_name = models.ForeignKey(Archive, on_delete=models.PROTECT, verbose_name= _("Arkivbeteckning"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("illustration")
        verbose_name_plural = _("illustrationer")


class Person(abstract.AbstractBaseModel, GenderedMixin):

    lastname = models.CharField(max_length=255, verbose_name= _("Efternamn"), blank=True, null=True)
    maidenname = models.CharField(max_length=255, verbose_name= _("Namn som ogift"), blank=True, null=True)
    firstname = models.CharField(max_length=255, verbose_name= _("Förnamn"), blank=True, null=True)
    birthday = models.CharField(max_length=255, verbose_name= _("Födelsedatum"), blank=True, null=True)
    deathday = models.CharField(max_length=255, verbose_name= _("Dödsdatum"), blank=True, null=True)
    birthplace = models.CharField(max_length=255, verbose_name= _("Födelseort"), blank=True, null=True)
    deathplace = models.CharField(max_length=255, verbose_name= _("Dödsort"), blank=True, null=True)
    wikidata = models.CharField(max_length=255, verbose_name= _("Wikidata ID"), blank=True, null=True)
    librisxl = models.CharField(max_length=255, verbose_name= _("Libris"), blank=True, null=True)
    article = models.TextField(verbose_name= _("Artikel"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Anteckningar"), blank=True, null=True)

    def __str__(self):
        return f"{self.lastname}"

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("personer")


class Place(abstract.AbstractBaseModel):
    placename = models.CharField(max_length=255, verbose_name= _("Ortnamn"), blank=True, null=True)
    geom = models.MultiPolygonField(verbose_name= _("Geometri"), blank=True, null=True)
    wikidata = models.CharField(verbose_name= _("Wikidata ID"), max_length=255, blank=True, null=True)
    parish_id = models.IntegerField(verbose_name= _("Församlingskod"), blank=True, null=True)
    municipality_id = models.IntegerField(verbose_name= _("Kommunkod"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("Anteckningar"), blank=True, null=True)


    def __str__(self):
        return f"{self.placename}"

    class Meta:
        verbose_name = _("Ort")
        verbose_name_plural = _("Orter")


# Do we need AbstractBaseModel or simple model?     
class RelIllustrEdition(models.Model):
    illustration_title = models.ForeignKey(Illustration, verbose_name= _("illustration title"), on_delete=models.PROTECT, blank=True, null=True)
    edition_title = models.ForeignKey(Edition, verbose_name= _("edition title"), on_delete=models.PROTECT, blank=True, null=True)


class RelPersonIllustration(models.Model):
    person_lastname = models.ForeignKey(Person, verbose_name= _("person lastname"), on_delete=models.PROTECT, blank=True, null=True)
    illustration_title = models.ForeignKey(Illustration, verbose_name= _("illustration title"), on_delete=models.PROTECT, blank=True, null=True)
    role = models.ForeignKey(Role, verbose_name= _("role"), on_delete=models.PROTECT, blank=True, null=True)


class RelPersonText(models.Model):
    person_lastname = models.ForeignKey(Person,verbose_name= _("person lastname"), on_delete=models.PROTECT, blank=True, null=True)
    sagatext_title = models.ForeignKey(SagaText,verbose_name= _("sagatext title"), on_delete=models.PROTECT, blank=True, null=True)
    role = models.ForeignKey(Role, verbose_name= _("role"), on_delete=models.PROTECT, blank=True, null=True)


class RelTextEdition(models.Model):
    sagatext_title = models.ForeignKey(SagaText,verbose_name= _("sagatext title"), on_delete=models.PROTECT, blank=True, null=True)
    edition_title = models.ForeignKey(Edition,verbose_name= _("edition title"), on_delete=models.PROTECT, blank=True, null=True)