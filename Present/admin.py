from django.contrib import admin
from .models import Teacher
# Register your models here.
admin.site.site_title = 'admin login'
admin.site.site_header = 'LOG-IN'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','email','online')
admin.site.register(Teacher,TeacherAdmin)