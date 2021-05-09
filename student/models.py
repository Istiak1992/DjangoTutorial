from django.db import models

# Create your models here.


class Department(models.Model):
	department_name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.department_name
	

class StudentInfo(models.Model):
	student_name = models.CharField(max_length=200, null=True, blank=True)
	id_no = models.BigIntegerField()
	department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
	Age = models.IntegerField()
	CGPA = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

	def __str__(self):
		return self.student_name

	