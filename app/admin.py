from django.contrib import admin
from django.utils.html import format_html

from .models import Resume
# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display =['id','name','role','location','experience','skills','organization',
    'salary','startdate','position','gap','age','qualification','my_file']

