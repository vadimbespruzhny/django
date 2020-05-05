from django.urls import path
from my_first_site.note import views

urlpatterns = [
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('cart_add_product/<int:product_id>',
         views.cart_add_product, name='cart_add_product'),
    path('cart_remove_all/<int:product_id>',
         views.cart_remove_all, name='cart_remove_all'),
    path('cart_remove/<int:product_id>',
         views.cart_remove, name='cart_remove'),
    path('search/', views.ObjectListView.as_view(), name='search_result'),
    path('product_delete/<int:pk>', views.product_delete,
         name='product_delete'),
    path('manufacturer_create', views.manufacturer_create,
         name='manufacturer_create'),
    path('manufacturer/<int:pk>', views.manufacturer_detail,
         name='manufacturer_detail'),
    path('product_create', views.product_create, name='product_create'),
    path('product_detail/<int:pk>', views.product_detail,
         name='product_detail'),
    path('monitor', views.monitor, name='monitor'),
    path('note', views.note, name='note'),
    path('', views.index, name='index'),
]
