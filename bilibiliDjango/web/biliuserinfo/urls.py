from django.urls import path, include
from .views import index
from .views import detail
from .views import png

urlpatterns = [
    path('', index),
    path('detail/<int:id>', detail),
    path('png', png),
]