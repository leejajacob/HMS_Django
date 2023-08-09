from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    department = models.ManyToManyField(Dept)
    doctorName = models.CharField(max_length=150)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
