from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="flight"),
    path("<int:flight_id>", views.flight, name="details"),
    path("<int:flight_id>/book", views.book, name="book"),

]