from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy

from .forms import AdminIronmongeryUpdateForm
from .models import Ironmongery
from applications.warehouse.models import Product, ProductCategory, ProductSubCategory


# Create your views here.
class IronmongeryDetailView(DetailView):
    template_name = "client/ironmongery/base.html"
    model = Ironmongery
    context_object_name = 'ironmongery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los productos asociados a la ferretería
        products = Product.objects.filter(fk_ironmongery=self.object)

        # Obtener categorías únicas de productos asociadas a la ferretería
        categories = ProductCategory.objects.filter(product__in=products).distinct()

        # Crear una lista de tuplas que contengan la categoría y un producto asociado
        categories_with_products = []
        for category in categories:
            product = products.filter(category=category).first()
            if product:
                categories_with_products.append((category, product))

        context['categories_with_products'] = categories_with_products
        return context


class ProductCategoryDetailView(DetailView):
    template_name = "client/ironmongery/ironmongery_product_list_category.html"
    model = Ironmongery
    context_object_name = "ironmongery"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la ferretería actual
        ironmongery = self.object

        # Obtener el ID de la categoría de la URL y convertirlo en un objeto ProductCategory
        pk_category = self.kwargs['pk_category']
        category = get_object_or_404(ProductCategory, pk=pk_category)

        # Obtener todas las subcategorías asociadas a la categoría que tienen al menos un producto
        subcategories_with_products = ProductSubCategory.objects.filter(
            fk_product_category=category,
            product__fk_ironmongery=ironmongery
        ).distinct()

        # Crear un diccionario para almacenar los productos asociados a cada subcategoría
        products_by_subcategory = {}
        for subcategory in subcategories_with_products:
            products = Product.objects.filter(
                fk_ironmongery=ironmongery,
                category=category,
                sub_category=subcategory
            )
            products_by_subcategory[subcategory] = products

        context['category'] = category
        context['products_by_subcategory'] = products_by_subcategory
        
        return context


class ClienteProductDetailView(DetailView):
    template_name = 'client/ironmongery/ironmongery_product_detail.html'
    model = Product


class AdminIronmongeyUpdateView(UpdateView):
    model = Ironmongery
    form_class = AdminIronmongeryUpdateForm
    template_name = 'custom_admin/ironmongery/ironmongery_update.html'
    success_url = reverse_lazy('userApp:user_list')




