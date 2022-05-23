from django.db import models

# Create your models here.

class Reg(models.Model):
	schoolmark =models.CharField(max_length=200)
	highschoolmark =models.CharField(max_length=200)
	collegename =models.CharField(max_length=200)
	cgpa =models.CharField(max_length=200)
	aadharno =models.CharField(max_length=200)
	phoneno =models.CharField(max_length=200)
	address =models.CharField(max_length=200)
	
