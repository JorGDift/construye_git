from django import forms
from applications.users.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label=' ',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '***********',
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data


class UserRegistrationForm(forms.Form):
    # datos del usuario
    user_email = forms.CharField(
        label='Correo',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'ej. correo@gmail.com',
                'class': 'form-control',
            }
        )
    )
    user_first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. Cesar Noe',
                'class': 'form-control',
            }
        )
    )
    user_last_name = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. Garcia Marquez',
                'class': 'form-control',
            }
        )
    )
    user_phone = forms.CharField(
        label='Numero de telefono',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. 322-123-43-23',
                'class': 'form-control',
            }
        )
    )
    user_password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '***********',
                'class': 'form-control',
            }
        )
    )
    user_password2 = forms.CharField(
        label='Confirmar contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '***********',
                'class': 'form-control',
            }
        )
    )

    # datos de dirección de la ferreteria
    ironmongery_city = forms.CharField(
        label='Ciudad',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. Puerto Vallarta',
                'class': 'form-control',
            }
        )
    )
    ironmongery_cologne = forms.CharField(
        label='Colonia',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. Los sauces',
                'class': 'form-control',
            }
        )
    )
    ironmongery_street = forms.CharField(
        label='Calle',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Av Gaviotas',
                'class': 'form-control',
            }
        )
    )
    ironmongery_postal_code = forms.CharField(
        label='Codigo Postal',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. 42602',
                'class': 'form-control',
            }
        )
    )
    ironmongery_outdoor_numer = forms.CharField(
        label='Numero de local',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. 385',
                'class': 'form-control',
            }
        )
    )

    # datos de la ferreteria
    ironmongery_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. La ferreteria de Cesar',
                'class': 'form-control',
            }
        )
    )
    ironmongery_logo = forms.ImageField(
        label='Logo',
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    ironmongery_phone = forms.CharField(
        label='Numero de telefono',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ej. 322-434-23-65',
                'class': 'form-control',
            }
        )
    )


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'firs_name', 'last_name', 'avatar', 'phone', 'password')

        widgets = {
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. alejandro@ejemplo.com',
                }
            ),
            'firs_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. Alejandro Daniel',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. Hernandez Garcia',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. 322-234-233-333',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '*************',
                }
            ),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'firs_name', 'last_name', 'avatar', 'phone', 'is_staff', 'is_active')

        widgets = {
            'avatar': forms.FileInput(
                attrs={
                    'class': 'form-control mt-1'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control mt-1'
                }
            ),
            'firs_name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1'
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input mt-1'
                }
            ),
            'is_staff': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input mt-1'
                }
            )
        }
        
    
class AdminUserSearchForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firs_name', 'email')

        widgets = {
            'firs_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. Alejandro Daniel',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ej. alejandro@gmail.com',
                }
            ),
        }