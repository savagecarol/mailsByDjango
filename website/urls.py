from .views import ind
from django.urls import path

urlpatterns = [
    path('',ind,name='home'),
#     path('mail/',index),
 ]
