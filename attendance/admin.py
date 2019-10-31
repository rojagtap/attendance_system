from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = EditProfileForm
    model = Faculty
    list_display = ['username', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'subject')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'subject')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'subject'),
        }),
    )


admin.site.register(Faculty, CustomUserAdmin)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Lecture)

admin.site.site_header = "SPIT Attendance Administrator"
admin.site.site_title = "SPIT Attendance Administrator"
