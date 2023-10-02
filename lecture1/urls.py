from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hello"),
    path("<str:name>", views.course, name="course-page"),
]