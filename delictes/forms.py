# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelChoiceField
from .models import Districte,Denuncia,Delicte
from supers.models import Super,Supervillano



class DenunciaForm(forms.Form):

    districte=forms.ModelChoiceField(queryset=Districte.objects.all(),empty_label='Tria Districte')
    supervillano=forms.ModelChoiceField(queryset=Supervillano.objects.all())
    observacions = forms.CharField(label="Alguna cosa a afegir??",widget=forms.Textarea)                    
   
