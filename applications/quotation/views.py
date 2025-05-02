from .models import Quotation, QuotationDetail
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class QuoteListView(ListView):
    model = Quotation
    context_object_name = "quote_list"
    paginate_by = 15
    template_name = "custom_admin/quote/quote_list.html"


class QuoteDetailView(DetailView):
    model = Quotation
    context_object_name = "quote"
    template_name = "custom_admin/quote/quote_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["detail_list"] = QuotationDetail.objects.search_details_quotation(quote_pk=self.kwargs.get("pk"))
        return context
