from django.urls import path

from . import views

app_name = "social-auth"

urlpatterns = [
    path("login/google/", views.GoogleLogin.as_view(), name="google-login"),
]