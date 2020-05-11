from .models import Order, OrderItem
from .forms import OrderCreationForm
from django.shortcuts import redirect, render
from .tasks import order_created


def order_create(request):
    order_obj = Order.objects.get(user=request.user, ordered=False)
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST, instance=order_obj)
        if form.is_valid():
            new_order = form.save()
            order_obj.ordered = True
            order_obj.save()
            order_items = order_obj.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.save()
            order_created.delay(new_order.pk)
            context = {'form': new_order, 'order_obj': order_obj}
            return render(request, 'order_created.html', context)
    else:
        form = OrderCreationForm()
        context = {'form': form, 'order_obj': order_obj}
        return render(request, 'order_create.html', context)


def order_detail(request):
    order = Order.objects.all()
    order_item = OrderItem.objects.all()
    context = {'order': order, 'order_item': order_item}
    return render(request, 'my_orders.html', context)
