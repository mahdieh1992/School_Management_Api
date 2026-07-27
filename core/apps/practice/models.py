from django.db import models
from ..school.models import BaseModel, School, ClassRoom
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Practice(BaseModel):
    """     
        Determin practices for students of the class 
    """
    title = models.CharField(max_length=150, help_text="title of practice")
    body = models.TextField(blank= True, null= True)
    deadline = models.DateTimeField()
    attachment = models.FileField(upload_to="upload_practice/", blank= True, null= True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="practice")
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="practice")
    
    class Meta:
        verbose_name= "Practice"
        verbose_name_plural = "Practices"
        
    def __str__(self):
        return f"{self.title}-{self.created_by}"
    
class PracticeAnswer(models.Model):
    """
     Representaion practice answers 
    """
    practice = models.ForeignKey(Practice, on_delete= models.CASCADE, related_name="practice_answer")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="practice_answer")
    answer = models.TextField(blank= True, null= True)
    attachment = models.FileField(upload_to="upload_practice/")
    
    class Meta:
        verbose_name = "Practice Answer"
        verbose_name_plural = "Practices Answer"
    
    def __str__(self):
        return f"{self.practice.title[:10]}-{self.user}"
    