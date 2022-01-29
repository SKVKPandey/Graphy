from django.shortcuts import render
from . models import Score

# Create your views here.

def index(request):
    
    data = Score.objects.all()
    print(Score.objects.all())

    context = {
        "data": data,
    }

    return render(request, 'lineChart/index.html', context)
