from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/<str:teacher_id>/', views.view_teacher, name='view_teacher'),

    path('teachers/edit/<str:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<str:teacher_id>/', views.delete_teacher, name='delete_teacher'),
]