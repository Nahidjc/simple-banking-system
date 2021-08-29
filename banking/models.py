from django.db import models

# Create your models here.


class registerUser(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False, unique=True, max_length=200)
    balance = models.IntegerField(blank=False)
    user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.email
