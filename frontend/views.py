from django.contrib.auth import logout, authenticate, login as django_login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from frontend.forms import LoginForm, RegisterForm
from frontend.models import CustomUser, Teacher, Bookin


class IndexView(View):
    def get(self, request):
        return render(request, 'frontend/index.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'frontend/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        error_message = []
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is None:
                error_message.append("Correo o contraseña incorrecta")
            else:

                if user.is_active:
                    django_login(request, user)
                    return redirect('dashboard')
                else:
                    error_message.append("El usuario no esta activo, ponte en contacto")

        context = {
            'errors': error_message,
            'form': form
        }
        return render(request, 'frontend/login.html', context)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'frontend/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        error_message = []
        if form.is_valid():
            first_name = form.cleaned_data.get('firstname')
            last_name = form.cleaned_data.get('lastname')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.filter(email=email)

            if user.count() > 0:
                error_message.append("Este correo ya está en uso")
            else:
                if first_name and last_name and email and password and phone:
                    user = User.objects.create_user(
                        username=email,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                    )
                    user_profile = CustomUser()
                    user_profile.user = user
                    user_profile.phone = phone
                    user_profile.save()
                    django_login(request, user)

                    return redirect('dashboard')

                else:
                    error_message.append("Complete el formulario de registro")
        context = {
            'errors': error_message,
            'form': form
        }
        return render(request, 'frontend/register.html', context)


class UserDashboard(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
            pass
        return render(request, 'frontend/dashboard.html')


class UserBooking(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        customuser = CustomUser.objects.get(user=request.user)
        bookings = Bookin.objects.filter(studen=customuser).all()

        context = {
            'bookings': bookings
        }
        return render(request, 'frontend/my_booking.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')


class SearchView(View):
    def get(self, request):
        query = request.GET['query']
        teachers = Teacher.objects.filter(
            Q(user__user__first_name__contains=query) | Q(user__user__last_name__contains=query) |
            Q(category__name__contains=query))

        context = {
            'techers': teachers,
            'query': query
        }

        return render(request, 'frontend/search.html', context)


class ProfileView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        context = {
            'teacher': teacher
        }
        return render(request, 'frontend/profile.html', context)


class BookingView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login')
        teacher = Teacher.objects.get(pk=pk)
        customuser = CustomUser.objects.get(user=request.user)
        context = {
            'teacher': teacher,
            'customuser': customuser
        }
        return render(request, 'frontend/bookin.html', context)


class PaymentView(View):
    def get(self, request, pk, method):
        if not request.user.is_authenticated:
            return redirect('login')
        teacher = Teacher.objects.get(pk=pk)
        customuser = CustomUser.objects.get(user=request.user)

        booking = Bookin()
        booking.ammount = teacher.ammount
        booking.studen = customuser
        booking.teacher = teacher
        booking.payment_method = method
        booking.bookint_to = request.GET.get('booking_to')
        booking.save()

        return redirect('dashboard')
