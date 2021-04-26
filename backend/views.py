from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


@ensure_csrf_cookie
def index(request):
  return render(request, 'index.html')
  
@ensure_csrf_cookie
def csrf(request):
  return { 'status': 'ok' }
# @ensure_csrf_cookie
class HomePageView(TemplateView):
    template_name = 'index.html'
