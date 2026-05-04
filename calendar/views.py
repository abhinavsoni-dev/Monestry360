from django.shortcuts import render
from django.http import HttpResponse

def calendar(request):
    try:
        return render(request, 'calendar/calendar.html')
    except Exception:
        return HttpResponse('Placeholder: calendar index')
    
def booking(request):
    return render(request, 'calendar/booking.html')
