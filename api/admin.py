from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudenAdmin(admin.ModelAdmin):
    lis_display = ['id','name','rool','city']
