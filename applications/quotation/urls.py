from django.urls import path
from . import views

app_name = 'quotationApp'

urlpatterns = [
    path('listado-de-cotizaciones/', views.QuoteListView.as_view(), name='admin_quote_list'),
    path('detalle-cotización/<int:pk>', views.QuoteDetailView.as_view(), name='admin_quote_detail'),
]