from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'first_name', 'last_name', 'gender', 'mobile_number')
    search_fields = ('teacher_id', 'first_name', 'last_name')
    list_filter = ('gender',)