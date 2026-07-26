from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active","is_registered")
    list_filter = ("is_staff", "is_active", "is_registered")
    search_fields = ("email", "national_code", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal_info"), {"fields": ("first_name", "last_name", "national_code")}),
        (_("Permissions"), {"fields": ("is_staff", "is_active", "is_superuser", "is_registered", "groups", "user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ( "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions")
        }),
    )
    
    search_fields = ("email",)
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user__email", "mobile_number","bio")