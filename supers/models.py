from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from geoposition import Geoposition


#classe abstracta SUPER.
class Super(models.Model):
    nom=models.CharField(verbose_name="Nom",max_length=100)
    superpoder=models.CharField(verbose_name="Superpoder",max_length=100)
    power=models.PositiveIntegerField(verbose_name="Powergeneration")
    position = GeopositionField()
    
    class Meta:
        abstract=True


#subclasse SUPERVILLANO
class Supervillano(Super):
    villano_id=models.IntegerField(primary_key=True)
 

#subclasse SUPERHEROI
class Superheroi(Super):
    heroi_id=models.IntegerField(primary_key=True)
    disponibilitat=models.DateTimeField()
    

