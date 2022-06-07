from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add_student, name="add_student"),
    path("list", views.list_Students, name="list_Students"),
    path("update/<Student_id>", views.update_Student, name="update_Student"),
    path("delete/<Student_id>", views.delete_Student, name="delete_Student"),
    path("search", views.search_Student, name="search_Student"),
    path("top", views.top_student, name="top_student"),
    path("search", views.search_name, name="search_name"),
]
