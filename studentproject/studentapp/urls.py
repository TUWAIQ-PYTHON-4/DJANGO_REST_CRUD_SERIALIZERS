from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("student/add", views.add_student, name="Add_student"),
    path("student/all", views.list_student, name="list_student"),
    path("student/update/<student_id>", views.update_student, name="update_student"),
    path("student/delete/<student_id>", views.delete_student, name="delete_student"),
    path("student/search/<first_name>", views.search, name="search"),
    path("student/order/", views.orderingviws, name="order")

]