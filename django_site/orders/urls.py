from django.urls import path
from . import views

urlpatterns = [
    path('order_create', views.order_create, name='order_create'),
    path('order_created', views.order_created, name='order_created'),
    # path('my_orders', views.order_detail, name='my_orders'),
]
