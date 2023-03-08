from django.core.mail import send_mail


def send_order_confirmation_code(email, code, name, price):
    
    full_link = f'Привет, подтвердите заказ на продукт {name}, сумма которого составила {price}\n\n http://localhost:8000/api/v1/order/confirm/{code}'

    send_mail(
    'Order from shop py25',
    full_link,
    'lucifercommander@gmail.com',
    [email]
    )