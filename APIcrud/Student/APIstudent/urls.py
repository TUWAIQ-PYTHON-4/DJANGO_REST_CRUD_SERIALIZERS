from django.urls import path
from . import views



urlpatterns = [
    path("add/", views.add_stu, name="add"),
    path("list/", views.list_stu, name="list"),
    path("put/<stu_id>", views.put_stu, name="put"),
    path("delete/<stu_id>", views.delete_stu, name="delete"),
    path("order/", views.order, name="order"),
    path("search/<stu_name>", views.search, name="search"),
]