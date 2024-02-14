from django.urls import path
from . import views

urlpatterns = [
path("sub_history/", views.sub_history, name="sub_history"),
path("", views.home, name="home")
]