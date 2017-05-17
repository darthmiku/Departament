from django.conf.urls import url
from . import views

app_name='delictes'

urlpatterns = [
     url(r'^denuncia/$',views.denuncia, name='denuncia'),
     

]