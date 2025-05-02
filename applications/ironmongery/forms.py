from django import forms


class AdminIronmongeryUpdateForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    ),
    logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
    banner = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
