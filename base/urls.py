from django.urls import path
from . import views

urlpatterns = [
    path('', views.rev_string, name="reverseString"),
]