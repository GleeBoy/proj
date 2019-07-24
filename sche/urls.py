from django.urls import path
from sche.views import *

urlpatterns = [
    path('schecount/',  schecount),
    path('addjob/', addjob),
    path('jobdetails/', jobdetails),

]