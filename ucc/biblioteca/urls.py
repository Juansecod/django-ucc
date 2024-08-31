from django.urls import path
from . import views

urlpatterns = [
    path("",  views.index, name="index"),
    path("sell", views.sell, name="sell"),
    path("lend", views.lend, name="lend"),
    path("sum/<int:n1>/<int:n2>", views.sum, name="sum"),
    path("calculator", views.calculator, name="calculator"),
]