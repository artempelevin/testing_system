from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def start_page_view(request: WSGIRequest) -> HttpResponse:
    return render(request=request,
                  template_name='main/start_page.html')

