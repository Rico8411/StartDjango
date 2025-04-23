from . import views
from django.urls import path

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('store/', store, name='about'),
    path('index/', index, name='about'),
    path('product/', product, name='about'),
    path('', index, name='about'),
]