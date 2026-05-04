from django.shortcuts import render
from django.http import HttpResponse

def archive(request):
    try:
        return render(request, 'archive/archive.html')
    except Exception:
        return HttpResponse('Placeholder: archive index')
