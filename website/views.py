from django.shortcuts import HttpResponse, render
from django.core.mail import send_mail
from django.conf import settings
from .models import Info
from django.views import View
import threading
from datetime import date
import time
class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/index.html')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        subject=request.POST.get('subject')
        text = request.POST.get('text')
        date = request.POST.get('date')
        c = Info(email=email, subject=subject,text=text, date=date)
        c.save()
        return render(request, 'website/index.html')



class Threading(object):
    def __init__(self):
        self.interval=2
        thread=threading.Thread(target=self.run,args=())
        thread.daemon=True
        thread.start()
    def run(self):
        while(True):
            today = date.today()
            print(Info.objects.all())
            k = Info.objects.filter(date=today)
            print(k)
            for i in k:
                send_mail(
                        i.subject,
                        i.text,
                        settings.EMAIL_HOST_USER,
                        [i.email],
                        fail_silently=False,
                        )
                print(i.email)
            Info.objects.filter(date=today).delete()
            print(Info.objects.all())
            time.sleep(self.interval)

example = Threading()

















#
# def ind(request):
#     if (request.method == 'POST'):
#         email=request.POST.get('email')
#         text =request.POST.get('text')
#         date = request.POST.get('date')
#         c=Info(email=email,text=text,date=date)
#         c.save()
#         return render(request, 'website/index.html')
#     return render(request, 'website/index.html')


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


