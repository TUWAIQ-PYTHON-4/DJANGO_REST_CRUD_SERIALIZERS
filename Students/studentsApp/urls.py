from django.urls import path
from . import views

urlpatterns = [
    path("displayStudents", views.display_students, name="display_students"),
    path('add_students', views.add_students, name='add_students'),
    path('update_student_info<int:id>', views.update_student_info, name='update_student_info'),
    path('delete_student<int:id>', views.delete_student, name='delete_student'),
    path('Search_by_name/<name>', views.Search_by_name, name='Search_by_name'),
    path('top_3_studens', views.top_3_studens, name='top_3_studens'),

]
