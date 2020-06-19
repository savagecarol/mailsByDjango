from .views import MyView
from django.urls import path

urlpatterns = [
    path('',MyView.as_view(),name='home'),
#     path('mail/',index),
 ]
