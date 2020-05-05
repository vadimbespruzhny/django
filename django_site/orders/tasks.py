
from django.core.mail import send_mail
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404
from .forms import OrderCreationForm
from my_site.celeryapp import app


@app.task
def order_created(pk):
    order_item = OrderItem.objects.all()
    for o in order_item:
        product = o.item
        quantity = o.quantity
    order = Order.objects.get(pk=pk)
    subject = 'Первый компьютерный супермаркет. Онлайн заказ № {}'.format(
        order.id)
    message = 'Номер заказа: № {}\n Товар: {}\n Количество: {}\n'.format(
        order.id, product, quantity)
    mail_sent = send_mail(
        subject, message, 'vadik654321@gmail.com', ['vadik654321@gmail.com'])
    return mail_sent

    # subject = 'Order nr'
    # message = 'You have successfully placed an order. Your order id is '
    # mail_sent = send_mail(subject, message, 'vadik654321@gmail.com', [
    #                       'vadik654321@gmail.com'])
    # return mail_sent

    # задача для отправки уведомления на почту при успешном создании заказа
