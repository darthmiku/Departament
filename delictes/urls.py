from django.conf.urls import url
from . import views

app_name='delictes'

urlpatterns = [
     url(r'^denuncia/$',views.denuncia, name='denuncia'),
     url(r'^list_denuncies/$',views.list_denuncies, name='list_denuncies'),
    

]