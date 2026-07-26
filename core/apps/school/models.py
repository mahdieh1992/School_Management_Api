from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class BaseModel(models.Model):
    """
        it is used to all model that want to use a base model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default= True, blank= True, help_text= "This object is active")
    
    class Meta:
        abstract= True
        
class School(BaseModel):
    """
        School model for storing school information
    """
    name = models.CharField(max_length= 150, help_text= "school name")
    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    
    class Meta:  
        verbose_name = "school"
        verbose_name_plural= "schools"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name= self.name.strip().title()
        return super().save(*args, **kwargs)
    
    

class Lesson(BaseModel):
    """ 
        Lesson model is used to storing lessons inforamtion
    """
    title = models.CharField(max_length= 150, help_text="Lesson name")
    code = models.IntegerField(unique= True)
    
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural= "Lessons"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.code += 5
        self.title = self.title.strip().title()
        return super().save(*args, **kwargs)
    
class ClassRoom(BaseModel):
    """
        Represents a classroom for a lesson in a school.
    """
    name = models.CharField(max_length= 150, help_text= "Class name")
    school = models.ForeignKey(School, on_delete= models.CASCADE, related_name="class_rooms")
    lesson = models.ForeignKey(Lesson, on_delete= models.CASCADE, related_name="class_rooms")
    teacher = models.ForeignKey(User, on_delete= models.CASCADE, related_name="teaching_classes")
    student = models.ManyToManyField(User, related_name="enrolled_classes")
    
    class Meta:
        verbose_name= "Class"
        verbose_name_plural= "Classes"
    
    def __str__(self):
        return self.name
    