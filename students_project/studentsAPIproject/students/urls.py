from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("add/", views.add_student, name="Add student"),
    path("all/", views.list_students, name="list_students"),
    path("update/<student_id>/", views.update_student, name="update_student"),
    path("delete/<student_id>/", views.delete_student, name="delete_student"),
    path("search/<first_name>/", views.search_student, name="search_student"),
    path("top/", views.top_3, name="top_3"),


]