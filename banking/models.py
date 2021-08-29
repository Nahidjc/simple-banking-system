from django.db import models

# Create your models here.


class registerUser(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False, unique=True, max_length=200)
    balance = models.IntegerField(blank=False)
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.email


class transferAmount(models.Model):
    sender = models.EmailField()
    receiver = models.EmailField()
    transfer_amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender + self.receiver
