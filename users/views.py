from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from users.forms import SignUpForm


class SignIn(LoginView):
    template_name = "users/signin.html"


class SignOut(LogoutView):
    pass


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "users/signup.html"
