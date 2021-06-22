from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class LoginView(View):
    def get(self, request):

        return render(request, 'frontend/login.html')


class RegisterView(View):
    def get(self, request):

        return render(request, 'frontend/register.html')