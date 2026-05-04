from django.shortcuts import render, redirect
from django.http import HttpResponse

# Step 1: Landing page with 3 tiers
def virtual_tours_tiers(request):
    return render(request, "tours/tiers.html")  
    # tiers.html -> shows Free (360), Recorded, Live tier options


# Step 2: Monastery selection (common page for all tiers)
def select_monastery(request, tier):
    context = {"tier": tier}
    return render(request, "tours/select_monastery.html", context)
    # select_monastery.html -> shows list of monasteries (links redirect based on tier)


# Step 3a: Free Tier - 360 photos
def view_360_photo(request, monastery_name):
    return render(request, "tours/view_360.html", {"monastery": monastery_name})


# Step 3b: Recorded walkthrough tours
def walkthrough_tour(request, monastery_name):
    return render(request, "tours/walkthrough.html", {"monastery": monastery_name})


# Step 3c: Live guided tour booking
def book_live_tour(request, monastery_name):
    return render(request, "tours/book_live.html", {"monastery": monastery_name})


# Step 3d: Join live tour (after booking/payment)
def join_live_tour(request, tour_code):
    return HttpResponse(f"You are joining live tour session: {tour_code}")



