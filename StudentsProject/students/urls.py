from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("student/add", views.create_student, name="create_student"),
    path("student/all", views.list_students, name="list_students"),
    path("student/update/<stu_id>", views.update_student, name="update_student"),
    path("student/delete/<stu_id>", views.delete_student, name="delete_student"),
    path("student/top", views.list_top_students, name="top_students"),
    path("student/search/<name>", views.search_student, name="search_student"),

]