from . import views
from django.urls import path

urlpatterns = [



    path("add/", views.add_stu, name="add"),
    path("list", views.list_stu, name="list"),
    path("update/<students_id>", views.edit_stu, name="update"),
    path("delete/<students_id>", views.del_stu, name="delete"),
    path("search/<first_name>", views.search_stu, name="search"),
    path("top/", views.list_top, name="search"),



]