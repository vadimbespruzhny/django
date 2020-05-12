
from django.core.mail import send_mail
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from .forms import OrderCreationForm
from my_site.celery import app


@app.task
def order_created(pk):
    order = Order.objects.get(pk=pk)
    order_item = OrderItem.objects.all()
    subject = f'Первый Компьютерный супермаркет. Онлайн заказ №: {order.pk}'
    message = f'Номер заказа {order.pk}\n Заказ: {order_item.item}\n Количество: {order_item.quantity}'
    mail_sent = send_mail(
        subject, message, 'vadik654321@gmail.com', [order.email])
    return mail_sent
