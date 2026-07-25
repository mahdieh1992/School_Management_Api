from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import timedelta
from django.utils import timezone
from .managers import CustomeUserManager

# Create your models here.

def curent_date():
    return timezone.now() + timedelta(days= 360 * 2)
    

class CustomUser(AbstractUser):
    """
        An abstract base class emplementing a fully feature for Custom User model
        Email and password is required 
    """
    email = models.EmailField(_("email address"), blank=True, unique= True)
    national_code = models.CharField(
        _("National Code"),
        max_length= 10,
        unique= True,
        validators=[
            MinLengthValidator(10),
            RegexValidator(
                regex= r'^\d{10}$',
                message= "National code must be exactly 10 digits"
            )
        ])
    
    date_expired = models.DateTimeField(_("Date Expired"), default=curent_date)
    is_registered = models.BooleanField(default= False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomeUserManager()
    
    def __str__(self):
        return self.email
    

class Profile(models.Model):
    """
        Profile model for store extra information users
    """
    class GenderChoice(models.TextChoices):
        female = "0", "Female"
        men = "1", "Men"
        
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE, related_name="profile")
    mobile_number = models.CharField(
        max_length= 11,
        blank= True,
        null= True,
        validators=[
           RegexValidator(
               regex= r'^\d{11}$',
               message= "Mobile number must be digit"
           )
        ])
    
    gender= models.CharField(max_length=1 , choices= GenderChoice, default=GenderChoice.female)
    image = models.ImageField(upload_to='profile_images/', blank= True, null= True)
    bio = models.TextField(blank= True, null= True)
    latitude = models.DecimalField(max_digits= 8, decimal_places= 3)
    longitude = models.DecimalField(max_digits= 8, decimal_places= 3)
    
    def __str__(self):
        return self.user.email
        