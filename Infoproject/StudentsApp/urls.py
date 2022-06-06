from django.urls import  path 
from . import views


app_name = 'studentsInfo'

urlpatterns = [

    path("student/all", views.list_student, name="list student"),
    path("student/add", views.add_students, name="Add student"),
    path("student/update/<student_id>", views.update_studet, name="update_studet"),
    path("student/delete/<student_id>", views.delete_student, name="update_studet"),

]

