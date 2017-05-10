# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm 
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from .models import Perfil,Ciutada
from delictes.models import Delicte,Denuncia,Districte
from django.conf import settings
from django.db.models import Q
from .forms import LoginForm,nou_usuari_form
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages


def dashboard(request):
     return render(request, 'dashboard.html')

#CREAR USUARI -------
def registrarse(request):
    
    #si el métode és POST--
    if request.method == 'POST':
        form = nou_usuari_form(request.POST )
        #si el contingut és vàlid
        if form.is_valid():
            username= form.cleaned_data['username']
            repetit = User.objects.filter( username = username )
            #mirem si està repetit i llencem missatge error "cuidadín"
            if repetit:
                messages.error( request, "Aquest nom d'usuari ja existeix a la base de dades")
            else:
                #ens quedem amb l'email i el password
                email= form.cleaned_data['email']
                password = form.cleaned_data['password']
                #creem el nou usuari
                nou_usuari = User.objects.create_user( username = username, email = email, password = password )
                #i creem el nou usuari
                ciutada=Ciutada.objects.create(perfil=nou_usuari.perfil)
                
                messages.info(request,"Usuari creat correctament")
                return redirect('usuaris:login')
    else:
        form = nou_usuari_form()
    
        for f in form.fields:
           form.fields[f].widget.attrs['class'] = 'input-group'
        
        form.fields['username'].widget.attrs['placeholder']="Username"   
        form.fields['email'].widget.attrs['placeholder']="Email"
        form.fields['password'].widget.attrs['placeholder']="Contrasenya"
        form.fields['username'].widget.attrs['required']="required" 
        form.fields['email'].widget.attrs['required']="required"
        form.fields['password'].widget.attrs['required']="required"
        
        return render(request, 'registrarse.html', {'form': form,} )

#LOGEJAR-SE ------
def login(request):

    #si tot es POST:
    if request.method=='POST':
        form=LoginForm( request.POST )

        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                              password = form.cleaned_data['password'])
               
            if user and user.is_active:
                #si tot és ok:
                authLogin( request, user )
                next = request.GET.get('next')
                messages.info(request,"Benvingut")
                return redirect(next or 'delictes:denuncia')

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
                
    else:
        form=LoginForm()
        ctx={ 'form':form, }
    # form.fields['username'].widget.attrs['placeholder']="Username"
    # form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    # form.fields['username'].widget.attrs['required']="required"
    # form.fields['password'].widget.attrs['required']="required"/
    
    return render(request, 'login.html', {} )

#DESLOGUEJAR-SE: me voy! ---    
def logout(request):
    authLogout( request )
    return redirect( 'usuaris:login')