from django.urls import path
from . import views

app_name = "todoList"
urlpatterns = [
    path("", views.lists, name="todos"),
    path("add", views.add, name="add"),
]
