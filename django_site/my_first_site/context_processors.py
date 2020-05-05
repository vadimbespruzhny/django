from orders.models import OrderItem


def order(request):
    order_count = OrderItem.objects.filter(ordered=False)
    return {'order_count': order_count}
