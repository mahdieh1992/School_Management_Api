from django.contrib import admin
from .models import MessageReceiver, Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display= ["text","sender","created_at"]
    search_fields = ["sender"]
    
@admin.register(MessageReceiver)
class MessageReceiverAdmin(admin.ModelAdmin):
    list_display= ["message","receiver", "is_read", "read_date"]
    list_filter = ["is_read"]
    search_fields = ["receiver"]
    
