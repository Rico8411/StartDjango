from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('store/', views.store, name='about'),
    path('index/', views.index, name='about'),
    path('product/', views.product, name='about'),
    path('', views.index, name='about'),
]