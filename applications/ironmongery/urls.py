from django.urls import path
from . import views

app_name = 'ironmongeryApp'

urlpatterns = [
    path('pagina-ferreteria/<int:pk>/', views.IronmongeryDetailView.as_view(), name='ironmongery_page'),
    path('productos-por-categoria/<int:pk>/<slug:pk_category>', views.ProductCategoryDetailView.as_view(), name='product_category_page'),
    path('detalle-del-producto/<int:pk>/', views.ClienteProductDetailView.as_view(), name='client_product_detail'),

    # administrador
    path('actualizar-ferreteria/<int:pk>/', views.AdminIronmongeyUpdateView.as_view(), name='admin_ironmongery_update'),
]