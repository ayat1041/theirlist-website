from django.urls import path
from .views import UserRegistrationView
# app_name = "app"

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
]