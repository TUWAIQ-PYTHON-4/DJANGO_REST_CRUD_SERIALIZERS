from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("list_students/", views.list_students, name="list students"),
    path("add_student/", views.add_student, name="Add student"),
    path("list_top3_students/", views.list_top3_students, name="list top 3 students"),
    path("search_student/<first_name>", views.search_student, name="search students"),
    path("update_student/<student_id>", views.update_student, name="update student"),
    path("delete_student/<student_id>", views.delete_student, name="delete student"),

]
