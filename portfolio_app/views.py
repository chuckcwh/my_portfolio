import json
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from portfolio import settings


def index(request):
    return render(request, 'index/index.html')

def blog(request):
    return render(request, 'blog.html')

@csrf_exempt
def email_send(request):
    say = 'Input Error. Please try again.'
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['name'] and data['message']:
            try:
                validate_email(data['email'])
                text_content = 'Name: {} Email: {}. Number: {}. Message: {}'.format(data['name'], data['email'], data['number'], data['message'])
                html_content = '<h2>Chuck\'s blog got a message!</h2>Name: {}<br>Email: {}<br>Number: {}<br>Message: {}'.format(data['name'], data['email'], data['number'], data['message'])
                msg = EmailMultiAlternatives("Blog got a new message!", text_content, settings.DEFAULT_FROM_EMAIL, ['content71@gmail.com'])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                say = 'Successfully Sent'
            except ValidationError:
                say = 'Please check the email format.'
        else:
            say = 'Please check the input.'
    return HttpResponse(
        json.dumps(say), content_type='application.json'
    )