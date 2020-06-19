from django.db import models

# Create your models here.

class UserInfo(models.Model):
	"""docstring for UserInfo"""
	first_name = models.CharField(max_length = 126)
	last_name = models.CharField(max_length = 126)
	email = models.EmailField(max_length = 260,unique = True)



