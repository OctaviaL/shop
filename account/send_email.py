from django.core.mail import send_mail


def send_activation_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'http://localhost:8000/api/v1/account/activate/{code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )

def send_password_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'Привет, чтобы сбросить пароль, тебе нужно знать этот токен: {code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )

