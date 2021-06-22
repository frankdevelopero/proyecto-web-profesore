from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('iniciar-sesion', LoginView.as_view(), name='login'),
    path('registro', RegisterView.as_view(), name='register'),

]
