from django.shortcuts import render
from django.views.generic import TemplateView

from applications.ironmongery.models import Ironmongery

from applications.users.forms import UserLoginForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "client/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexContentView(TemplateView):
    template_name = "client/content.html"
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ironmongery_list'] = Ironmongery.objects.search_ironmongery()
        return context

    


class LoginView(TemplateView):
    template_name = "client/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_login_form'] = UserLoginForm
        return context
