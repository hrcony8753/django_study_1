from django.db import models

# Create your models here.
class Member(models.Model):
	name=models.CharField(max_length=50, default="unknown")
	age=models.IntegerField(default='20')
	phone=models.CharField(max_length=50, default="010-0000-0000")

	user_id=models.CharField(max_length=50, default="unknown")
	user_psw=models.CharField(max_length=50, default="unknown")

	def __str__(self):
		return self.name
		
class Post(models.Model):
	title=models.CharField(max_length=100, default="unknown")
	description=models.CharField(max_length=100, blank=True, help_text='simple description text')
	content=models.TextField(max_length=500, default="unknown")

	def __str__(self):
		return self.title