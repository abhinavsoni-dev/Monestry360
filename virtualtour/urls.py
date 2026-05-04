from django.urls import path
from . import views

app_name = 'virtualtour'
urlpatterns = [
    # Step 1: Landing page with 3 tiers
    path("tours/", views.virtual_tours_tiers, name="virtual_tours_tiers"),

    # Step 2: Monastery selection (tier passed in URL)
    path("tours/select/<str:tier>/", views.select_monastery, name="select_monastery"),

    # Step 3: Service pages (depends on tier & monastery chosen)
    path("tours/360/<str:monastery_name>/", views.view_360_photo, name="view_360_photo"),
    path("tours/walkthrough/<str:monastery_name>/", views.walkthrough_tour, name="walkthrough_tour"),
    path("tours/live/book/<str:monastery_name>/", views.book_live_tour, name="book_live_tour"),

    # Live session join link
    path("tours/live/join/<str:tour_code>/", views.join_live_tour, name="join_live_tour"),

    
]
