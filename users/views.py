from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignUpForm


class SignIn(LoginView):    # Вход
    template_name = "users/signin.html"
    success_url = reverse_lazy('test_suites')


class SignOut(LogoutView):  # Выход
    pass


class SignUp(CreateView):   # Регистрация
    form_class = SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy('signin')
