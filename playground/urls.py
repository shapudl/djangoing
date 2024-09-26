from django.urls import path
from . import views

urlpatterns = [
    path("hello/random/", views.say_random_stuff),
    path("hello/", views.say_hello)
]