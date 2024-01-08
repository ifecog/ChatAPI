from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'last_login', 'is_staff', 'is_active',)
    list_display_links = ('first_name', 'last_name', 'email')
    list_filter = ('email', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'display_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'phone_number', 'password2', 'first_name', 'last_name', 'display_picture')
        }),
        ('permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )
    search_fields = ('email',)
    ordering = ('email',)
    

admin.site.register(User, UserAdmin)