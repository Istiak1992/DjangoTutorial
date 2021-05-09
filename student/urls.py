from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name='home'),
    path('createdept/', createDepartment, name='createdepartment'),
    path('createstudent/', createStudentInfo, name='createstudent'),
    path('showDept/', showDepartment, name='showDept'),
    path('updateDept/<int:id>/', updateDepartment, name='updateDept'),
    path('deleteDept/<int:id>/', deleteDepartment, name='deleteDept'),
    path('showStudent/', showStudentInfo, name='showStudent'),
    path('upadateStudent/<int:id>/',upadateStudentInfo, name='upadateStudentInfo'),
    path('deleteStudent/<int:id>/',deleteStudentInfo, name='deleteStudent'),
    
]
