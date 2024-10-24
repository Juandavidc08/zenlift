from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    payment_status = models.BooleanField(default=False)  # New field to track payment

    def __str__(self):
        return f"{self.user.username} - {self.trainer.name} on {self.date} at {self.time}"
