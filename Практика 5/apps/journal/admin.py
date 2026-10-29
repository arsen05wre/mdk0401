from django.contrib import admin
from .models import Student, Subject, Grade, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","class_name","email")
    list_filter = ("class_name",)
    search_fields = ("last_name","first_name")
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name","teacher")
    search_fields = ("name","teacher")
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student","subject","mark","date")
    list_filter = ("mark","subject","date")
    search_fields = ("student__last_name","subject__name")
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student","subject","date","status")
    list_filter = ("status","subject","date")
