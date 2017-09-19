from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone_no = models.CharField(max_length = 50)
	
	address = models.TextField(null=True, blank=True)
	city = models.CharField(max_length = 50, null= True, blank = True)
	pincode = models.IntegerField(null= True, blank = True)

	

