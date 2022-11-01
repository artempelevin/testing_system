from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from main.models import TestSuite


class TestSuiteListView(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_REDIRECT_URL
    model = TestSuite
    template_name = 'main/test_suites.html'
