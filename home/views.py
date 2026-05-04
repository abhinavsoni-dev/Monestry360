from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import booking  

# Home page
def home(request):
    try:
        return render(request, 'home.html')
    except Exception:
        return HttpResponse('Placeholder: home index')
    
def booking(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        arrival_date = request.POST.get('arrival_date')
        arrival_time = request.POST.get('arrival_time')
        departure_date = request.POST.get('departure_date')
        departure_time = request.POST.get('departure_time')

        booking_info = booking(first_name=first_name, last_name=last_name, email=email, phone=phone,
                               arrival_date=arrival_date, arrival_time=arrival_time,
                               departure_date=departure_date, departure_time=departure_time)
        booking_info.save()
        return redirect('home')  # Redirect to home page after booking
    return render(request, 'booking.html')
