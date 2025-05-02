from django import forms
from applications.warehouse.models import ProductCategory, Brand, ProductSubCategory, Product


class ProductCreateForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ej. Taladro',      
            }
            
        ),
        label="Nombre del Producto",
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'ej. Agrega una descripción para el producto',    
            }
        ),
        label="Descripcion"
    )
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'ej. Herramientas',    
            }
        ),
        label="Categoria"
    )
    sub_category = forms.ModelChoiceField(
        queryset=ProductSubCategory.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'ej. Taladros',   
            }
        ),
        label="Sub Categoria"
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control'}
        ),
        label="Imagen"
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ej. 2,699',   
            }
        ),
        label="Precio"
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'ej. Cat',   
            }
        ),
        label="Marca"
    )


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'sub_category', 'price', 'status', 'brand')

        labels = {
            "name": ("Nombre del Producto"),
            "description": ("Descripcion"),
            "image": ("Imagen"),
            "category": ("Categoria"),
            "sub_category": ("Sub Categoria"),
            "price": ("Precio"),
            "status": ("Estatus"),
            "brand": ("Marca"),
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control mt-1',
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control mt-1',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'sub_category': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'brand': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            )
        }
        
        
class AdminProductSearchForm(forms.ModelForm):    
    class Meta:
        model = Product
        fields = ('name','category', 'sub_category', 'status', 'brand')

        labels = {
            "name": ("Nombre del Producto"),
            "category": ("Categoria"),
            "sub_category": ("Sub Categoria"),
            "status": ("Estatus"),
            "brand": ("Marca"),
        }        
        
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1',
                    'placeholder':'ej. Taladro',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'sub_category': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            ),
            'brand': forms.Select(
                attrs={
                    'class': 'form-select mt-1',
                }
            )
        }
    
    category_initial = 3  # Reemplaza 'valor_por_defecto' por el valor que deseas que sea el predeterminado

    def __init__(self, *args, **kwargs):
        super(AdminProductSearchForm, self).__init__(*args, **kwargs)
        self.fields['category'].initial = self.category_initial