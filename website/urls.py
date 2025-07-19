from django.urls import path
from . import views


app_name = "website"
urlpatterns = [
    path("calculation", views.calculator_view, name="calculation"),
    path("", views.index, name="index"),
    path("/about", views.about, name="about"),
    path("/contact", views.contact, name="contact"),
]
