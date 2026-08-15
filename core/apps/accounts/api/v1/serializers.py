from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as validator
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from ...models import Profile

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ("email", "password","confirm_password", "first_name", "last_name", "national_code")
        
    def validate(self, attrs):
        try:
            validator.validate_password(attrs['password'])
        except Exception as e:
            raise serializers.ValidationError(list(e.messages))
        
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("password and confirm_password must be equal")
        
        return attrs
        
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("id","email", "first_name", "last_name", "national_code", "is_registered")
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')  
        user = authenticate(email = email , password= password)
        if not user:
            raise serializers.ValidationError("email or passwor is not correct")
        return user
    
    
class ChangPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    new_password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only = True)

    def validate(self, attrs):
        user = self.context['request'].user
        new_password = attrs['new_password']
        confirm_password= attrs['confirm_password']
        old_password = attrs['old_password']
        if not check_password(old_password, user.password):
            raise serializers.ValidationError({"old_password": "Old password is not correct."})
        elif new_password != confirm_password:
            raise serializers.ValidationError({"new_password and confirm_password must be equal"})
        else:
            try:
                validator.validate_password(new_password)
            except Exception as e:
                raise serializers.ValidationError({"detail": list(e.messages)})
            return attrs
        
class ProfileUserSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source = "user.email", read_only = True)
    class Meta:
        model = Profile
        fields = ["user","mobile_number", "gender", "image", "bio", "latitude", "longitude"]
       
                
                
            