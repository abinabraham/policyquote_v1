from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.accounts.models import User


@admin.register(User)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", 
    				"dob",)
    list_filter = ("is_active", )
    search_fields = ("first_name__startswith",
    				 "last_name__startswith",)