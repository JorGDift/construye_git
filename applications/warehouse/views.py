from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from applications.warehouse.forms import ProductCreateForm, ProductUpdateForm, AdminProductSearchForm

from django.views.decorators.http import require_GET

from .models import Product


# Create your views here.
class ProductCreateView(FormView):
    template_name = 'custom_admin/product/product_create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('warehouseApp:admin_product_list')

    def form_valid(self, form):
        Product.objects.create_product(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image'],
            category=form.cleaned_data['category'],
            sub_category=form.cleaned_data['sub_category'],
            price=form.cleaned_data['price'],
            brand=form.cleaned_data['brand'],
            fk_ironmongery=self.request.user.fk_ironmongery,
        )

        messages.add_message(self.request, messages.INFO, f"Producto creado correctamente")
        return super(ProductCreateView, self).form_valid(form)


class AdminProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    paginate_by = 15
    template_name = "custom_admin/product/product_list.html"    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_search"] = AdminProductSearchForm
        return context
    
    def get_queryset(self):
        
        fk_ironmongery = self.request.user.fk_ironmongery
        
        if self.request.GET:
            name = self.request.GET.get("name", '')
            status = self.request.GET.get("status", 0)
            category = self.request.GET.get("category", '')
            sub_category = self.request.GET.get("sub_category", '')
            brand = self.request.GET.get("brand", '')
            
            return Product.objects.admin_search_product(fk_ironmongery, name, status, category, sub_category, brand)
        
        return Product.objects.filter(fk_ironmongery=fk_ironmongery)
    
class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "custom_admin/product/product_detail.html"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'custom_admin/product/product_update.html'
    success_url = reverse_lazy('warehouseApp:admin_product_list')
    

class AdminProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('warehouseApp:admin_product_list')


@require_GET
def search_products_view(request):
    if request.method == 'GET':
        if 'promp' in request.GET:
            prompt = request.GET['promp']
            product_list = Product.objects.search_products(prompt)
            results = [{'id': product.id, 'ironmongery': product.fk_ironmongery.name, 'name': product.name, 'price': product.price, 'image': product.image.url} for product in product_list]

            return JsonResponse(results, safe=False)
        else:
            return JsonResponse({'error': 'Formulario no valido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    


    