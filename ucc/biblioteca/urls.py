from django.urls import path
from . import views

urlpatterns = [
    path("",  views.index, name="index"),
    path("blue", views.view_blue, name="view_blue")
]