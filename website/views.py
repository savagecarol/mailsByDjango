from django.shortcuts import HttpResponse,render
from django.core.mail import send_mail
from django.conf import settings

def ind(request):
    return render(request, 'website/index.html')


# def index(request):
#     time.sleep(120)
#     send_mail(
#         'Subject here',
#         'Here is the message.',
#         settings.EMAIL_HOST_USER,
#         ['karthiksharma1411@gmail.com'],
#         fail_silently=False,
#     )
#     return HttpResponse("mail has been send")

# def job():
#     print("Reading time..")
#
#
# schedule.every(10).seconds.do(job)
# while(True):
#     schedule.run_pending()
#     time.sleep(1)
#
