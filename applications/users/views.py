from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, FormView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# usuarios y autenticación
from django.contrib.auth import authenticate, login, logout

from .forms import UserUpdateForm, UserCreateForm, UserLoginForm, UserRegistrationForm, AdminUserSearchForm

from .models import User

from applications.ironmongery.models import Ironmongery, IronmongeryLocation
from .. import ironmongery


# Create your views here.
class UserLoginView(FormView):
    form_class = UserLoginForm
    success_url = reverse_lazy('userApp:user_list')

    def form_valid(self, form):
        # se authentica el usuario
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)

        return super(UserLoginView, self).form_valid(form)


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'client/user_register.html'
    success_url = reverse_lazy('userApp:user_list')

    def form_valid(self, form):
        # se crean los datos de direccion de la ferreteria
        ironmongery_address = IronmongeryLocation.objects.create_ironmongery_address(
            city=form.cleaned_data['ironmongery_city'],
            cologne=form.cleaned_data['ironmongery_cologne'],
            street=form.cleaned_data['ironmongery_street'],
            postal_code=form.cleaned_data['ironmongery_postal_code'],
            outdoor_number=form.cleaned_data['ironmongery_outdoor_numer'],
        )

        # Se crea la ferreteria
        ironmongery = Ironmongery.objects.create_ironmongery(
            name=form.cleaned_data['ironmongery_name'],
            logo=form.cleaned_data['ironmongery_logo'],
            fk_location=ironmongery_address,
            phone=form.cleaned_data['ironmongery_phone'],
        )

        # Se crea el usaurio
        User.objects.create_user(
            email=form.cleaned_data['user_email'],
            firs_name=form.cleaned_data['user_first_name'],
            last_name=form.cleaned_data['user_last_name'],
            phone=form.cleaned_data['user_phone'],
            fk_ironmongery=ironmongery,
            password=form.cleaned_data['user_password'],
        )

        messages.add_message(self.request, messages.INFO, f"Welcome")
        return super(UserRegistrationView, self).form_valid(form)


class UserCreateView(FormView):
    template_name = 'custom_admin/user/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('userApp:user_list')

    def form_valid(self, form):
        User.objects.create_staff(
            avatar=form.cleaned_data['avatar'],
            email=form.cleaned_data['email'],
            firs_name=form.cleaned_data['firs_name'],
            last_name=form.cleaned_data['last_name'],
            phone=form.cleaned_data['phone'],
            fk_ironmongery=self.request.user.fk_ironmongery,
            password=form.cleaned_data['password'],
        )

        messages.add_message(self.request, messages.INFO, f"Usuario agregado correctamente")
        return super(UserCreateView, self).form_valid(form)


class UserListView(ListView):
    model = User
    context_object_name = 'user_list'
    paginate_by = 15
    template_name = 'custom_admin/user/user_list.html'

    def get_queryset(self):
        ironmongery = self.request.user.fk_ironmongery
        
        if self.request.GET:
            firs_name = self.request.GET.get("firs_name", '')
            email = self.request.GET.get("email", '')
            
            return User.objects.filter(fk_ironmongery=ironmongery, firs_name__icontains=firs_name, email__icontains=email)
        
        return User.objects.search_user_by_ironmongery(ironmongery)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_search_form"] = AdminUserSearchForm
        return context
    

class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = "custom_admin/user/user_detail.html"


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'custom_admin/user/user_update.html'
    success_url = reverse_lazy('userApp:user_list')
    

class AdminUserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('userApp:user_list')

