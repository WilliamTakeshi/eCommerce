from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Product
from carts.models import Cart


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
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
