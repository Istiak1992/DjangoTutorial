from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import DepartmentForm, StudentInfoForm
from .models import Department, StudentInfo
from .filters import FilterStudentInfo


# Create your views here.

def home(request):

	return HttpResponse('<h1>Welcome Home</h1>')



def createDepartment(request):
	form = DepartmentForm()

	if request.method=='POST':
		form = DepartmentForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponse('Data Saved.')
	else:
		form = DepartmentForm()

	context = {'form': form}

	return render(request, 'student/createdept.html', context)


def createStudentInfo(request):
	form = StudentInfoForm()

	if request.method=='POST':
		form = StudentInfoForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponse('Data Saved.')
	else:
		form = StudentInfoForm()

	context = {'form': form}

	return render(request, 'student/createstudent.html', context)


def showDepartment(request):
	departments = Department.objects.all()

	context = {'departments': departments}
	return render(request, 'student/showDept.html', context)

def updateDepartment(request,id):
	obj = get_object_or_404(Department, id=id)

	
	if request.method=='POST':
		form = DepartmentForm(request.POST, instance=obj)
		if form.is_valid:
			form.save()
			return HttpResponse('Sucessfully Updated.')

	else:
		form = DepartmentForm(instance=obj)

	context = {'form':form}
	return render(request, 'student/updateDept.html', context)

def deleteDepartment(request, id):
	obj = get_object_or_404(Department, id=id)

	if request.method=='POST':
		obj.delete()
		return HttpResponse('Sucessfully deleted.')

	context={'obj':obj}

	return render(request, 'student/deleteDept.html', context)




def showStudentInfo(request):
	students = StudentInfo.objects.all()

	context = {'students':students}
	return render(request, 'student/showStudent.html', context)



def upadateStudentInfo(request,id):
	obj = get_object_or_404(StudentInfo, id=id)

	if request.method=='POST':
		form = StudentInfoForm(request.POST, instance=obj)

		if form.is_valid:
			form.save()
			return HttpResponse('Successfully Upadated')

	else:
		form = StudentInfoForm(instance=obj)

	context = {'form':form}

	return render(request, 'student/updateStudent.html', context)



def deleteStudentInfo(request, id):
	obj = get_object_or_404(StudentInfo, id=id)

	if request.method=='POST':
		obj.delete()
		return HttpResponse('Successfully Deleted.')

	context = {'obj': obj}
	return render(request,'student/deleteStudent.html', context)



def searchStudentInfo(request):

	students = StudentInfo.objects.all()
	filters = FilterStudentInfo(request.GET, queryset=students)

	context = {'filters': filters}

	return render(request, 'student/searchStudent.html', context)






