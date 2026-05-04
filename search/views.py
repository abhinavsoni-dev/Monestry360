from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    try:
        return render(request, 'search/index.html')
    except Exception:
        return HttpResponse('Placeholder: search index')
