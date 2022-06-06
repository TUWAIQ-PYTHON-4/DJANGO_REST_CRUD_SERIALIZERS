from django.urls import path
from . import views


urlpatterns = [

    path("student/add", views.add_student, name="Add studenty"),
    path("students/all", views.list_student, name="list student"),
    path("update/<student_id>", views.update_student, name="update_student"),
    path("delete/<student_id>", views.delete_students, name="delete_students"),
    path("top3", views.top3_student, name="top3_student"),
    path("search", views.search_name, name="search_name"),

]