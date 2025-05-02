from django.urls import path
from . import views

app_name = 'coreApp'

urlpatterns = [
    path("", views.IndexContentView.as_view(), name="Inicio"),
    path("Index/", views.IndexView.as_view(), name="Index"),
    path("Login/", views.LoginView.as_view(), name="Login"),

]