from django.shortcuts import HttpResponse,render
from django.core.mail import send_mail
from django.conf import settings
from .models import Info
def ind(request):
    if (request.method == 'POST'):
        email=request.POST.get('email')
        text =request.POST.get('text')
        date = request.POST.get('date')
        c=Info(email=email,text=text,date=date)
        c.save()
        return render(request, 'website/index.html')
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
