from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('iniciar-sesion', LoginView.as_view(), name='login'),
    path('cerrar-sesion', LogoutView.as_view(), name='logout'),
    path('registro', RegisterView.as_view(), name='register'),
    path('mi-cuenta', UserDashboard.as_view(), name='dashboard'),
    path('mi-cuenta/clases', UserBooking.as_view(), name='bookings'),
    path('buscar', SearchView.as_view(), name='search'),
    path('perfil/<int:pk>', ProfileView.as_view(), name='profile'),
    path('reservar/<int:pk>', BookingView.as_view(), name='book'),
    path('pagar/<int:pk>/<int:method>', PaymentView.as_view(), name='payment'),

]
