
from django.urls import path
# from django.conf.urls import url,include

from . import views
urlpatterns = [
    
    path("",views.index,name="home"),
    # path("/pdf-to-jpg/",views.super,name="super")
    path("pdf-to-jpg/", views.super1, name='proj'),
    path("pdf-to-jpg/", views.super2, name='proj'),


]
