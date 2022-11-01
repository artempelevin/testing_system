from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from main.models import Test


class TestsListView(LoginRequiredMixin, ListView):
    login_url = settings.LOGIN_REDIRECT_URL
    model = Test
    template_name = 'main/test_suite.html'

    def get_queryset(self):
        test_suite_id_: int = self.kwargs['test_suite_id']
        return Test.objects.filter(test_suite_id=test_suite_id_)
