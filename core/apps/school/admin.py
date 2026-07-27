from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ClassRoom, School, Lesson


User = get_user_model()
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name", "latitude", "longitude", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]

@admin.register(ClassRoom)
class classAdmin(admin.ModelAdmin):
    list_display= ["name", "school", "lesson", "teacher", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "code", "formatted_code", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["title", "code"]
    
    @admin.display(description= "Lesson Code")
    def formatted_code(self, obj):
        return f"LS-{obj.code:08d}"