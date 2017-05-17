# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuaris.models import Perfil
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from django.utils.encoding import python_2_unicode_compatible
from geoposition import Geoposition


#classe abstracta SUPER.
class Super(models.Model):
    nom=models.CharField(verbose_name="Nom",max_length=100)
    superpoder=models.CharField(verbose_name="Superpoder",max_length=100)
    power=models.PositiveIntegerField(verbose_name="Powergeneration")
    districte = models.ForeignKey('delictes.Districte')
    # position = GeopositionField()
    
    class Meta:
        abstract=True



#subclasse SUPERVILLANO
@python_2_unicode_compatible
class Supervillano(Super):
    villano_id=models.IntegerField(primary_key=True)
    aparensa=models.CharField(max_length=200,verbose_name='Aparença')
    graumaldat=models.CharField(verbose_name="Grau de Maldat",max_length=50)
    
    #per retornar el nom
    def __str__(self):
        return self.nom
    

#subclasse SUPERHEROI
@python_2_unicode_compatible
class Superheroi(Super):
    heroi_id=models.IntegerField(primary_key=True)
    disponibilitat=models.DateTimeField()
    perfil = models.OneToOneField(Perfil,default="")
    
    #per retornar el nom
    def __str__(self):
        return self.nom



