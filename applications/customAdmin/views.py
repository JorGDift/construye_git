from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from applications.warehouse.models import Product

# Create your views here.
class AdminDashboardView(TemplateView):
    template_name = "custom_admin/base.html"
    
