from __future__ import unicode_literals

from django.db import models
from usuaris.models import Perfil
from supers.models import Superheroi


class Districte(models.Model):
    nom=models.CharField(max_length=200)
    
    #per retornar el nom
    def __str__(self):
        return self.nom


#DENUNCIA
class Denuncia(models.Model):
    data=models.DateTimeField(auto_now_add=True)
    districte=models.ForeignKey(Districte,on_delete=models.CASCADE,)
    supervillano=models.ForeignKey('supers.Supervillano',on_delete=models.CASCADE)
    observacions=models.CharField(max_length=200,default="", blank=True)


#DELICTE
class Delicte(models.Model):
    denuncia=models.OneToOneField(Denuncia,on_delete=models.CASCADE,)
    policia=models.ForeignKey('usuaris.Perfil',on_delete=models.CASCADE,)
    superheroi=models.ForeignKey('supers.Superheroi',)
    haGuanyatelBe=models.NullBooleanField()

    
