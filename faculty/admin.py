from django.contrib import admin
from .models import Faculty, JobTitle, Subject

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name','job_title',)

class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Subject, SubjectAdmin)