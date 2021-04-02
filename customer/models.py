from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
