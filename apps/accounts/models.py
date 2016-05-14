from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=100, default='That guy')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	class Meta:
		db_table = 'users'