from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()

class Message(models.Model):
    """
    Represents a message sent by a user.
    """
    text = models.TextField(blank= True, null= True)
    sender = models.ForeignKey(user, on_delete= models.CASCADE, related_name="message")
    created_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return self.sender.email
    
    
class MessageReceiver(models.Model):
    """
        Tracks the recipients of a message and their read status.
    """
    message = models.ForeignKey(Message, on_delete= models.CASCADE, related_name="message_receiver")
    receiver = models.ForeignKey(user, on_delete= models.CASCADE, related_name="message_receiver")
    is_read = models.BooleanField(default= False)
    read_date = models.DateTimeField(blank= True, null= True)
    
    class Meta:
        verbose_name = "Message Receiver"
        verbose_name_plural = "Messages Receivers"
        
    def __str__(self):
        return self.receiver.email
    
