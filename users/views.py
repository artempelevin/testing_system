from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignUpForm


class SignIn(LoginView):
    success_url = reverse_lazy("login")
    template_name = "users/signin.html"


class SignOut(LogoutView):
    # success_url = reverse_lazy("login")
    template_name = "users/signout.html"


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"
