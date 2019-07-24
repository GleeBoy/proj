from django.urls import path
from cele.views import *

urlpatterns = [
    path('studySessions/',  studySessions),

]