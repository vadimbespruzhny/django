from django.shortcuts import render, get_object_or_404, redirect
from my_first_site.note.models import Product, Manufacturer
from my_first_site.note.forms import NotebookForm, ManufacturerForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.db.models import Q
from django.utils import timezone
from orders.models import OrderItem, Order
from orders.tasks import order_created
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
# Create your views here


def index(request):
    return render(request, 'index.html')


def paginate(request, category, num_items):
    paginator = Paginator(category, num_items)
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    context = {'paginator': paginator, 'notes': notes}
    return context


def note(request):
    note_category = Product.objects.filter(category__iexact='note')
    pagin = paginate(request, note_category, 6)
    context = {'note_category': note_category,
               'pagin': pagin}
    return render(request, 'note/templates/note.html', context)


def monitor(request):
    monitor_category = Product.objects.filter(category__iexact='mon')
    context = {'monitor_category': monitor_category}
    return render(request, 'note/templates/monitor.html', context)


def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    context = {'manufacturer': manufacturer}
    return render(request, 'note/templates/manufacturer_detail.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'note/templates/product_detail.html', context)


def product_create(request):
    form = NotebookForm()
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('note'))
    else:
        return render(request, 'note/templates/product_create.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('note'))
    else:
        return render(request, 'note/templates/product_delete.html', {'product': product})


def manufacturer_create(request):
    form = ManufacturerForm()
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('products'))
    else:
        return render(request, 'note/templates/manufacturer_create.html', {'form': form})


def cart_add_product(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    # создаем объект заказа
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    # получаем список заказов конкретного пользователя
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            # если есть, увеличиваем кол-во на 1
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Кол-во товара в корзине обновлено')
            return redirect('cart_detail')
        else:
            # если нет, в заказ добавляем единицу товара
            order.items.add(order_item)
            messages.info(request, 'Товар добавлен в корзину')
            return redirect('cart_detail')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'Товар добавлен в корзину')
        return redirect('cart_detail')


def cart_remove(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, 'Товар удален из корзины')
            else:
                order_item.delete()
                messages.info(request, 'Товар удален из корзины')
    return redirect('cart_detail')


def cart_remove_all(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    order_query_set = Order.objects.filter(
        user=request.user, ordered=False)
    if order_query_set:
        # получаем первый заказ пользователя
        order = order_query_set[0]
        # проверяем есть ли единица товара в заказе
        if order.items.filter(item=item.id):
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order_item.delete()
            messages.info(request, 'Товар удален из корзины')
            return redirect('order_create')
        else:
            return redirect('cart_detail')
    return redirect('cart_detail')


def cart_detail(request):
    order = Order.objects.get(
        user=request.user, ordered=False)
    context = {'order': order}
    return render(request, 'cart_detail.html', context)


class ObjectListView(ListView):
    model = Product
    template_name = 'search_result.html'

    def get_queryset(self):
        # получаем список объектов модели Product
        queryset = Product.objects.all()
        query = self.request.GET.get('q')
        if query:
            return queryset.filter(Q(name__icontains=query))
        return queryset
