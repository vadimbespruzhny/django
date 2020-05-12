
from django.core.mail import send_mail
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from .forms import OrderCreationForm
from my_site.celery import app


@app.task
def order_created(pk):
    order = Order.objects.get(user=request.user, ordered=True)
    subject = f'Первый Компьютерный супермаркет. Онлайн заказ №: {order.pk}'
    message = f'Номер заказа \n Заказ:  \n Количество:'
    mail_sent = send_mail(
        subject, message, 'vadik654321@gmail.com', ['vadik654321@gmail.com'])
    return mail_sent
