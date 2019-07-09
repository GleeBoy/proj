from django.urls import path, include
from .views import *

urlpatterns = [
    path('schecount/',  schecount),
    path('addjob/', addjob),
    path('jobdetails/', jobdetails),

]