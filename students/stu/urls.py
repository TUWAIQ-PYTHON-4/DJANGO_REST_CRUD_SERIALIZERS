from django.urls import path
from . import views


urlpatterns = [
    path("stu/add", views.add_stu, name="Add Stu"),
    path("stu/all", views.list_stu, name="list Stu"),
    path("stu/update/<student_id>", views.update_stu, name="update_stu"),
    path("stu/delete/<pk>", views.delete_stu, name="delete_stu"),
]