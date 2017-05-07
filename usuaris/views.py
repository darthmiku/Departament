# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm 
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from .models import Perfil
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages











# Create your views here.
def login(request):

    
    return render(request, 'login.html')
    
#DESLOGUEJAR-SE: me voy! ---    
def logout(request):
    authLogout( request )
    return redirect( 'login.html')