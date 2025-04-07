from django.contrib import admin
from django.urls import path
from shope1.views import about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about)
]
