from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
def get_message(request):
    if request.is_ajax():
        name = request.GET.get('name' ,None)
        email = request.GET.get('email' ,None)
        text = request.GET.get('text' ,None)
        print(name, email, text)
        if name and email and text:
            # now send the mail to the user mail

            message_to_admin = 'You got new message from ' + name + '! \nPlease reply soon as possible as on ' + email + '\nMessage: '+text
            subject = 'Thank you for contacting us'
            # body = get_template('mail.html').render(ctx)

            body = 'Thank you for contacting us, ' + name + '\nWe will contact you soon! Sinc. www.novusorg.com LPU \n-----------------\nYour message: '+text

            email_to_user = EmailMessage(subject=subject, body=body, to=[email])
            email_to_user.send()

            email = EmailMessage(subject='You have one more message from site', body=message_to_admin, to=['novusorg.lpu@gmail.com'])

            email.send()

            print('mail sent')
            return JsonResponse({'message':'Thanks, we will contact you soon!'})

