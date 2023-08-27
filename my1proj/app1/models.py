from django.db import models

class Contestants(models.Model):
    lastname = models.CharField(max_length=30, blank=False)
    firstname = models.CharField(max_length=30, blank=False)
    midname = models.CharField(max_length=30, blank=False)
    institution = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=16, blank=False)
    email = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f'{self.lastname} {self.firstname[0]}. {self.midname[0]}'