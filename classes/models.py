from django.db import models

from people.models import Student, Ucitel

class Skupina(models.Model):
	name = models.CharField(max_length=200)
	studenti = models.DecimalField(max_digits=5, decimal_places=0)
	a = [] 
	for i in intermediate_count(studenti):
		a += models.ForeignKey(Ucitel, on_delete=models.CASCADE)
	# # all_student = models.ForeignKey(Student, on_delete=models.CASCADE)
	# for Students in Student.object.all():
	# 	a += models.ForeignKey(Ucitel, on_delete=models.CASCADE)
	def __str__(self):
		return self.name