from django.conf.urls import url
from . import views

app_name='usuaris'

urlpatterns = [
  #  url(r'^menu/$', views.menu_usuari,name="menu_usuari"),
  url(r'^$', views.login, name='login'),
  url(r'^logout/$', views.logout, name='logout'),
  url(r'^registrarse/$',views.registrar_ciutada,name='registrar_ciutada'),
  url(r'^dashboard/$', views.dashboard, name="dashboard"),
   
]

