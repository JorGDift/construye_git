from django.urls import path
from . import views

app_name = 'warehouseApp'

urlpatterns = [
    path('crear-producto/', views.ProductCreateView.as_view(), name='admin_product_create'),
    path('listado-de-productos/', views.AdminProductListView.as_view(), name='admin_product_list'),
    path('detalle-del-producto/<int:pk>/', views.ProductDetailView.as_view(), name='admin_product_detail'),
    path('editar-producto/<int:pk>/', views.ProductUpdateView.as_view(), name='admin_product_update'),
    path('eliminar-producto/<int:pk>/', views.AdminProductDeleteView.as_view(), name='admin_product_delected'),
    path('buscar-producto/', views.search_products_view, name='client_search_product'),
]
