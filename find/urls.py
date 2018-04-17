from django.urls import path
from .views import FindProductView


app_name = 'find'
urlpatterns = [
    path('', FindProductView.as_view(), name='query'),
]
