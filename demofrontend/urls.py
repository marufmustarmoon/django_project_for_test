from django.urls import path
from .views import *

urlpatterns = [

    path("", home),
    
    path("home/", home),

    path("add/", add),
    
    path("delete/<int:id>", deletee),
    
    path("addd/<int:id>", addd),
    
    path("getupdate/<int:id>", getupdate),
    
   

]
  