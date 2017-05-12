# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Crearem el PERFIL de l'usuari: OneToOne amb USER de DJANGO que pa eso està
class Perfil(models.Model):
    # 1 to 1 - model User
    usuari = models.OneToOneField(User,related_name='perfil')

    def es_policia(self):
         return hasattr(self,'policia')

    def es_ciutada(self):
        return hasattr(self, 'ciutada')
    
    def es_superheroi(self):
        return hasattr(self,'superheroi')


@python_2_unicode_compatible
class Ciutada(models.Model):
    perfil = models.OneToOneField(Perfil)
    
    def __str__(self):
        return "Id: %s usuari: %s"%(self.id, self.perfil.user.username)

class Policia(models.Model):
    num_placa=models.CharField(max_length=5)
    perfil= models.OneToOneField(Perfil)


def post_save_user(sender, instance, created, **kwargs):
    if created:
        nou_perfil = Perfil.objects.create(
                    usuari=instance,
                    )
        instance.refresh_from_db()

post_save.connect(post_save_user, sender=User)