from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    date = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "date": date.month == 1 and date.day == 1
    })
