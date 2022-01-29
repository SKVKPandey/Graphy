from django.shortcuts import render
from . models import Scores

# Create your views here.

def index(request):
    
    data = Scores.objects.all()
    print(Scores.objects.all())

    context = {
        "data": data,
    }

    return render(request, 'lineChart/index.html', context)