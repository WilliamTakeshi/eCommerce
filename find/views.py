from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
# Create your views here.


class FindProductView(ListView):

    template_name = "find/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
