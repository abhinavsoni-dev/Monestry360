from django.shortcuts import render
from django.http import HttpResponse

def maps(request):
    try:
        return render(request, 'monasteries/maps.html')
    except Exception:
        return HttpResponse('Placeholder: Monasteries Map')

def rumtek(request):
    try:
        return render(request, 'monasteries/rumtek.html')
    except Exception:
        return HttpResponse('Placeholder: Rumtek Monastery')
    
def tsechey(request):
    try:
        return render(request, 'monasteries/tsechey.html')
    except Exception:
        return HttpResponse('Placeholder: Tsechey Monastery')
    
def tsukla(request):
    try:
        return render(request, 'monasteries/tsukla.html')
    except Exception:
        return HttpResponse('Placeholder: Tsukla Monastery')   
     
def pemayangtse(request):
    try:
        return render(request, 'monasteries/pemayangtse.html')
    except Exception:
        return HttpResponse('Placeholder: Pemayangtse Monastery')
