from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('all_students/', views.all_students, name='all_students'),
    path('update_student/<student_id>/', views.update_student, name='update_student'),
    path('delete_student/<student_id>/', views.delete_student, name='delete_student'),
    path('top_students/', views.top_students, name='top_students'),
    path('search/', views.search, name='search')
]
