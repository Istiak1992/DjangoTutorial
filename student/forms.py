from django.forms import ModelForm
from .models import Department, StudentInfo


class DepartmentForm(ModelForm):
	class Meta:
		model = Department
		fields = ['department_name']


class StudentInfoForm(ModelForm):
	class Meta:
		model = StudentInfo
		fields = ['student_name','id_no','department', 'Age', 'CGPA']