from django.urls import path
from . import views

urlpatterns = [
    path("student/add", views.add_student, name="Add student"),
    path("student/all", views.all_students, name="list students"),
    path("student/update/<student_id>", views.update_student, name="update student"),
    path("student/delete/<student_id>", views.delete_student, name="delete student"),
    path("student/top3", views.top_3, name="top 3 students"),
    path("student/search", views.search_student, name="search")
]