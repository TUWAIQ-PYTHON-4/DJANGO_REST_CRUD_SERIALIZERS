from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("add/", views.add_student, name="add_student"),
    path("list_all/", views.list_students, name="list_students"),
    path("update/<student_id>", views.update_student, name="update_student"),
    path("delete/<student_id>", views.delete_student, name="delete_student"),
    path("search/<f_name>", views.search, name="search"),
    path("top3/", views.top3, name="top3"),
]
