from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("add_student", views.add_student, name="add_student"),
    path("list_student", views.list_student, name="list_student"),
    path("update_student/<students_id>", views.update_student, name="update_student"),
    path("delete_student/<students_id>", views.delete_student, name="delete_student"),
    path("best_student_grade", views.best_student_grade, name="best_student_grade"),
]
