from django.urls import path
from . import views



urlpatterns = [
    path("new_student/", views.new_student, name="new_student"),
    path("list_student/", views.list_student, name="list_student"),
    path("update_student/<student_id>", views.update_student, name="update_student"),
    path("delete_student/<student_id>", views.delete_student, name="delete_student"),
    path("search/<first_name>", views.search, name="search"),
    path("List_top_GPA/", views.List_top_GPA, name="List_top_GPA"),

]