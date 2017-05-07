# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from delictes.models import Delicte,Denuncia,Districte
from supers.models import Super,Superheroi,Supervillano
from usuaris.models import Perfil
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import DenunciaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.
def crear_denuncia(request):
    # usuari=Perfil.objects.get(id=usuari_id)
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
           districte= form.cleaned_data['districte']
           supervillano = form.cleaned_data['supervillano']
           observacions=form.cleaned_data['observacions']

        #creem l'objecte DENUNCIA amb les dades rebudes
        Denuncia.objects.create(    districte=districte,
                                    supervillano=supervillano,
                                    observacions=observacions,
                                       )   
        messages.info(request,"denúncia creada correctament")
        return redirect("delictes:crear_denuncia")    
    else:
        form= DenunciaForm()
        
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'formulari'
 
    return render (request, 'delictes/dashboard.html', {'form': form} )    

   
# #EDITAR DISC EXISTENT
# def editar_disc(request, oferta_disc_id):
#     EditForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere','estat','descripcio','preu', 'image'))
#     unEdit = Oferta_disc()
#       #comprovem que existeix l'oferta_disc
#     if oferta_disc_id:
#         unEdit = get_object_or_404(Oferta_disc, pk=oferta_disc_id)
        
#     if request.method == 'POST':
#         form = EditForm (request.POST,request.FILES, instance= unEdit)
#         if form.is_valid():
#           form.save()
#           messages.info(request,"disc canviat correctament")
#           return redirect("usuaris:login.html")    
#     else:
#         form= EditForm (instance = unEdit)
    
#     for f in form.fields:
#         form.fields[f].widget.attrs['class'] = 'formulari'
 
#     form.fields['titol'].widget.attrs['placeholder']="Titol"
#     form.fields['grup'].widget.attrs['placeholder']="Grup"
#     form.fields['anny'].widget.attrs['placeholder']="Any"
#     form.fields['descripcio'].widget.attrs['placeholder']="Descripció"
#     form.fields['preu'].widget.attrs['placeholder']="Preu"
    
#     return render (request, 'discos/editar_disc.html', {'form': form} )  