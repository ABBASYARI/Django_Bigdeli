from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog_view, name="blog"),
    path("single", views.single_view, name="single"),
]
