"""testing_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import start_page_view, TestSuiteListView, TestsListView, QuestionsListView

urlpatterns = [
    path('', start_page_view, name='index'),
    path('test_suites/', TestSuiteListView.as_view(), name='test_suites'),
    path('test_suites/<int:test_suite_id>/', TestsListView.as_view(), name='test_suite'),
    path('test_suites/<int:test_suite_id>/tests/<int:test_id>/', QuestionsListView.as_view(), name='test'),
]
