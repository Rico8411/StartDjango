from django.contrib import admin
from django.urls import path, include
from shop.views import index,store,product,checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('shop/', include('shop.urls')),

    # path('checkout/', checkout, name='checkout'),
    # path('store/', store, name='store'),
    # path('index/', index, name='index'),
    # path('product/', product, name='product'),
    # path('', index, name='home'),
]
