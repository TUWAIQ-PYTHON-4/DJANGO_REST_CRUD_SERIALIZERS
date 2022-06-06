from django.urls import path
from . import views

app_name = "StudentApp"

urlpatterns = [
    path("add/", views.add_student, name="add_student"),
    path("all/", views.list_student, name="list_student"),
    path("update/<student_id>/", views.update_student, name="update_student"),
    path("delete/<student_id>/", views.delete_student, name="delete_student"),
    path("top/", views.list_top3, name="list_top3"),
    path("search/<str:first_name1>/", views.search_std, name="search_std"),
]