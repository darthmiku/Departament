# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from delictes.models import Delicte,Denuncia,Districte
from supers.models import Super,Superheroi,Supervillano
from usuaris.models import Perfil
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 
# Create your views here.



# Create your views here.
