from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def studySessions(request):
    print(request.session.get_expire_at_browser_close())
    return HttpResponse('study session')