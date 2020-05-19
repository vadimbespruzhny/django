from .models import Order, OrderItem
from .forms import OrderCreationForm
from django.shortcuts import redirect, render
from .tasks import order_created_task


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
            order_created_task.delay(order_obj.pk)
            return redirect('order_created')
            # return render(request, 'order_created.html', context)
    else:
        form = OrderCreationForm()
        context = {'form': form, 'order_obj': order_obj}
        return render(request, 'order_create.html', context)


def order_created(request):
    new_order = Order.objects.all()
    for n in new_order:
        n = n
    return render(request, 'order_created.html', {'new_order': n})

# def order_detail(request):
#     order = Order.objects.select_related().get(user=request.user)
#     new_order = order.items.all()
#     for i in new_order:
#         context = {
#             'order': order,
#             'new_order': new_order,
#             'i': i,
#         }
#         return render(request, 'my_orders.html', context)
