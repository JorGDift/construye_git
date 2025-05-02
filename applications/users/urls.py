from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('login-usuario/', views.UserLoginView.as_view(), name='user_login'),
    path('registrar-usuario/', views.UserRegistrationView.as_view(), name='user_register'),
    path('agregar-usuario/', views.UserCreateView.as_view(), name='user_create'),
    path('listado-de-usuarios/', views.UserListView.as_view(), name='user_list'),
    path('detalle-de-usuario/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('actualizar-usuario/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
    path('eliminar-usuario/<int:pk>', views.AdminUserDeleteView.as_view(), name='admin_user_deleted'),
]
