from django.urls import path
from . import views

app_name = "FirstRestApp"

urlpatterns = [
    path("date/", views.date, name="date"),
    path("random/", views.random, name="random"),
    path('add_student/', views.add_student, name='add_student'),
    path("list_students/", views.list_students, name='list_students'),
    path("update_student/<student_id>", views.update_student, name="update_student"),
    path("delete_student/<student_id>", views.delete_student, name="delete_student"),
    path("list_top_students/", views.list_top_students, name='list_top_students'),
    path('search_for_student/<str:student_first_name>/<str:student_last_name>/', views.search_for_student,
         name="student_first_name ,student_last_name")

]