from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name', 'location')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'profile', 'company')
    search_fields = ('emp_name', 'profile', 'company')
    list_filter = ('company',)


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
