from django.shortcuts import render
from . models import T1Score, T2Score
# Create your views here.

def index(request):
      ins1 = T1Score(Level="lvl1",point=50)
      ins1.save()
      ins2 = T2Score(Level="lvl1",point=40)
      ins2.save()
      data1=T1Score.objects.all()
      data2=T2Score.objects.all()
      context = {
        "data1": data1,
        "data2": data2,
      }
      print(context['data1'])
      print(context)
      return render(request, 'lineChart/index.html', context)
