from django.db import models
from ..school.models import ClassRoom, BaseModel
from django.contrib.auth import get_user_model

user = get_user_model()
class News(BaseModel):
    """
        News model for each class 
    """
    title = models.CharField(max_length= 150, help_text="Title of new")
    body = models.TextField(blank= True, null= True)
    created_by = models.ForeignKey(user, on_delete= models.CASCADE, related_name= "news")
    class_room = models.ForeignKey(ClassRoom, on_delete= models.CASCADE, related_name="news")
    
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
        
    def __str__(self):
        return self.title
    
    
class NewsReceiver(BaseModel):
    """
    Represent news receiver model for each class
    """
    news = models.ForeignKey(News, on_delete= models.CASCADE, related_name="receiver")
    student = models.ForeignKey(user, on_delete=models.CASCADE, related_name="receiver")
    is_read = models.BooleanField(default= False)
    read_date= models.DateTimeField(blank= True, null= True)
    
    class Meta:
        verbose_name = "News Receiver"
        verbose_name_plural = "News Receivers"
        
    def __str__(self):
        return f"{self.student.email} - {self.news.title}"
    
