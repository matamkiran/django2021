from django.contrib import admin
# Register your models here.
from myappdemo.models import EmployeeDemo
from myappdemo.models import SutdentDemo
# Register your models here.

admin.site.register(EmployeeDemo)
admin.site.register(SutdentDemo)
