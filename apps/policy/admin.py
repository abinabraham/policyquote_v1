from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.policy.models import Quote, Policy, AgeBand, PolicyType



admin.site.register(AgeBand)
admin.site.register(PolicyType)


@admin.register(Quote)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("quote", "customer", "types", "status",)
    list_filter = ("customer","status")
    search_fields = ("customer__first_name__startswith",
    				 "quote__startswith",)

@admin.register(Policy)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "types", "age_band","is_active",)
    list_filter = ("types","is_active","age_band")
    search_fields = ("name__startswith",
    				 "types__type_name__startswith",)