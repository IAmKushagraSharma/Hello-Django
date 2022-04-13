from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email =  models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fname
    