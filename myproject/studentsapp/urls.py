from django.urls import path
from . import views

app_name= "studentsapp"

urlpatterns = [
    path("students/add", views.add_student, name="Add student"),
    path("students/all", views.list_students, name="list students"),
    path("students/update/<student_id>", views.update_student, name="update_student"),
    path("students/delete/<student_id>", views.delete_student, name="delete_student"),
    path("students/top3", views.top_3, name="top 3 students"),
    path("students/search", views.search_student, name="search")
]