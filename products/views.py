from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "products/list.html"


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductFeaturedDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context