from django.db import models

# Create your models here.
class Info(models.Model):
    email=models.EmailField(blank=False)
    subject=models.TextField()
    text=models.TextField(blank=False)
    date=models.DateField(blank=False)
    def __str__(self):
        return self.email




