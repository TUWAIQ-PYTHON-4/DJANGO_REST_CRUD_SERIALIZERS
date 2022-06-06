from django.urls import path
from . import views 




urlpatterns = [
    path("add", views.add_student, name="Add-student"),
    path("all/", views.list_students, name="list-student"),
    path("update/<student_id>", views.update_student, name="update-student"),
    path("delete/<student_id>", views.delete_student, name="delete-student"),
    path("top/", views.list_top3, name="list_top3"),
    path("search/<name>", views.search_std, name="search"),


]