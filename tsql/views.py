from django.shortcuts import render
import random
from tsql.models import Record
from django.db.models import Max

# Create your views here.


def random_insert():
    i = 0
    while True:
        Record.objects.create(img_path=str(random.choice(range(9999999999999))), user_id=random.choice(range(100)))
        i += 1
        j = i % 1000
        if j == 0:
            print(i)




