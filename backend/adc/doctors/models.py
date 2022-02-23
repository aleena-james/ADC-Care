from django.db import models

# Create your models here.
class Doctors(models.Model):
    ROLE = (
			('Doctor', 'Doctor'),
			('Staff', 'Staff'),
			
			)
    dname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    role = models.CharField(max_length=200, null=True,choices=ROLE)
    specialisation = models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)

    def __str__(self):
	    return self.dname
