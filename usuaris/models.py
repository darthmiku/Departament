from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Perfil(models.Model):
    # 1 to 1 - model User
    usuari = models.OneToOneField( User,related_name='Perfil')
    es_policia=models.BooleanField(default=False)
    es_admin=models.BooleanField(default=False)
    es_ciutada=models.BooleanField(default=False)
    es_superheroi=models.BooleanField(default=False)
    
    def __unicode__(self):
		return "Id: %s usuario: %s"%(self.id, self.user.username)
    
def post_save_user(sender, instance, created, **kwargs):
    if created:
        nou_perfil = Perfil.objects.create(
                    usuari=instance,
                    )
        instance.refresh_from_db()

post_save.connect(post_save_user, sender=User)