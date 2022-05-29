
from django.urls import path
# from django.conf.urls import url,include

from . import views
urlpatterns = [
    
    path("",views.index,name="home"),
    # path("/pdf-to-jpg/",views.super,name="super")
    path("inpaint/", views.inpainting, name='proj'),
    path("super_resolution/", views.super_res, name='proj'),
    path("about/", views.about, name='proj'),


]
