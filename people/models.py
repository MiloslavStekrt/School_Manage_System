from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=200)
	number = models.DecimalField(max_digits=9, decimal_places=0)
	email = models.EmailField(max_length=254)
	home_address = models.TextField()
	password = models.CharField(max_length=200)
	year_study = models.DecimalField(max_digits=60, decimal_places=0)

class Ucitel(models.Model):
	name = models.CharField(max_length=200)
	number = models.DecimalField(max_digits=9, decimal_places=0)
	email = models.EmailField(max_length=254)
	home_address = models.CharField(max_length=200)
	let_ve_skole = models.DecimalField(max_digits=75, decimal_places=2)
	nastup = models.DateTimeField(auto_now=True)