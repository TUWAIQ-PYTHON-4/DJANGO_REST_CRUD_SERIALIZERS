from django.urls import path
from . import views

urlpatterns = [
path("add/", views.add_std, name="Add Student"),
path("show/", views.std_list, name="Show Student"),
path("update/<std_id>", views.update_stds_info, name="update Information"),
path("delete/<std_id>", views.delete_std, name="delete student Information"),
path("top/", views.top_studenrs, name="Top Student"),

]