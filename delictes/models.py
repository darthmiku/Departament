from __future__ import unicode_literals

from django.db import models
from usuaris.models import Perfil
from supers.models import Superheroi


# #----> cap a la migracio
# DISTRICTE_CHOICES = (      
#                             ( 'D1-NORD GOTHAM', 'D1-Nord Gotham'),
#                             ( 'D2-GOTHAM CENTRE', 'D2-Gotham Centre'),
#                             ( 'D3-ARKHAM CITY', 'D3-Arkham City'),
#                             ( 'D4-GOTHAM EAST', 'D4-Gotham East '),
#                             ( 'D5-GOTHAM SUD', 'D5-Gotham Sud'),
#                             ( 'D6-BRONX GOTHAM', 'D6-Bronx GOTHAM')
                   
#                         )

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

    
