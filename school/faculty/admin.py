from django.contrib import admin
from .models import Teacher, Department, Holiday  

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'first_name', 'last_name', 'gender', 'mobile_number')
    search_fields = ('teacher_id', 'first_name', 'last_name')
    list_filter = ('gender',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_teacher')
    search_fields = ('name',)
    filter_horizontal = ('teachers',)

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    search_fields = ('name',)
    list_filter = ('date',)
