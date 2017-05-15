# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelChoiceField
from .models import Districte,Denuncia,Delicte



class DenunciaForm(forms.Form):

    districte=forms.ModelChoiceField(queryset=Districte.objects.all())
    supervillano=forms.CharField(max_length=200, label='Supervillano')
    observacions = forms.CharField(label="Alguna cosa a afegir??",widget=forms.Textarea)                    
   
