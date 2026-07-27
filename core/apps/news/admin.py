from django.contrib import admin
from .models import News, NewsReceiver

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display= ["title", "body", "created_by", "class_room", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["title"]
    
@admin.register(NewsReceiver)
class NewsReceiverAdmin(admin.ModelAdmin):
    list_display= ["news", "student", "is_read", "read_date", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]
    search_fields = ["news"]