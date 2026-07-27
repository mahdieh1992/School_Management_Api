from django.contrib import admin
from .models import Practice, PracticeAnswer

# Register your models here.
@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display= ["title","class_room", "created_by", "created_at", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["title"]
    
@admin.register(PracticeAnswer)
class PracticeAnswerAdmin(admin.ModelAdmin):
    list_display= ["practice", "user"]
    search_fields = ["user"]