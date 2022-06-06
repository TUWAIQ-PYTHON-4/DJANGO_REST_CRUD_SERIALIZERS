from django.urls import path
from . import views



urlpatterns = [
    path("add/", views.add_student, name="add"),
    path("all", views.list_student, name="list"),
    path("update/<students_id>", views.update_student, name="update"),
    path("delete/<students_id>", views.delete_student, name="delete"),
    path("search/<first_name>", views.search_student, name="search"),
    path("top/", views.top3_GPA, name="search"),




    ]