# -*- coding: utf-8 -*-
from django import forms


#Formulari per CREAR LA DENUNCIA d'un malhechor
class DenunciaForm (forms.Form):
    DISTRICTE_CHOICES = (
                            ( 'D1-NORD GOTHAM', 'D1-Nord Gotham'),
                            ( 'D2-GOTHAM CENTRE', 'D2-Gotham Centre'),
                            ( 'D3-ARKHAM CITY', 'D3-Arkham City'),
                            ( 'D4-GOTHAM EAST', 'D4-Gotham East '),
                            ( 'D5-GOTHAM SUD', 'D5-Gotham Sud'),
                            ( 'D6-BRONX GOTHAM', 'D6-Bronx GOTHAM')
               
                        )
    districte=forms.CharField(label="districte",max_length=200,widget=forms.Select(choices=DISTRICTE_CHOICES),)
    supervillano=forms.CharField(label='supervillano',max_length=200)
    observacions= forms.CharField(label="observacions",widget=forms.Textarea)
   