from django.contrib import admin
from .models import Student, Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('student', 'address_type', 'address',)

admin.site.register(Address, AddressAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name',)

admin.site.register(Student, StudentAdmin)
