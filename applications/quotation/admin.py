from django.contrib import admin
from .models import Quotation, QuotationDetail

# Register your models here.
admin.site.register(Quotation)
admin.site.register(QuotationDetail)


