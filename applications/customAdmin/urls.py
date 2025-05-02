from django.urls import path
from . import views

app_name = 'customAdminApp'

urlpatterns = [
    path('dashboard/', views.AdminDashboardView.as_view(), name='dashboard'),
]