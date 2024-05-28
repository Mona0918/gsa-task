from django.db import models
from django.contrib.auth.models import User, AbstractUser

class RegisterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.IntegerField()
    address = models.TextField()
    longitude = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.CharField(max_length=500, null=True, blank=True)

class DepratmentUser(models.Model):
    DEPT = (('finance','finance'),
            ('sales','sales'),
            ('testing','testing'),
            ('devleopment','devleopment'))
    department = models.CharField(max_length=255, choices=DEPT)
    user=models.CharField(max_length=500)

    def __str__(self):
        return f'{self.user} - {self.department}'


class TaskAssign(models.Model):
    user = models.ForeignKey(DepratmentUser, on_delete=models.CASCADE)
    assigned_by = models.CharField(max_length=500)
    task_name=models.CharField(max_length=500)
    date=models.DateField()
    time=models.TimeField()
