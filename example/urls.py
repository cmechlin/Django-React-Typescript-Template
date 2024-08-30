from django.urls import path

# importing views from views..py
from .views import example_view

urlpatterns = [
    path("", example_view),
]
