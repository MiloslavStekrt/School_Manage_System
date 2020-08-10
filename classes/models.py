from django.db import models

from people.models import Student, Ucitel

class Skupina(models.Model):
	name = models.CharField(max_length=200)
	ucitel = models.ForeignKey(Ucitel, on_delete=models.CASCADE)
	all_student = models.ForeignKey(Student, on_delete=models.CASCADE)