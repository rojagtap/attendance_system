from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = EditProfileForm
    model = Faculty
    list_display = ['username', 'first_name', 'last_name']


admin.site.register(Faculty, CustomUserAdmin)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Lecture)

admin.site.site_header = "SPIT Attendance Administrator"
admin.site.site_title = "SPIT Attendance Administrator"
