from django.shortcuts import render
from . models import T1Score, T2Score

# Create your views here.

def index(request):
    data1 = T1Score.objects.all()
    data2 = T2Score.objects.all()

    context = {
        "data1": data1,
        "data2": data2
    }

    return render(request, 'lineChart/index.html', context)