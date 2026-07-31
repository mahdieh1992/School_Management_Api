from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "national_code","password", "password1"]
        extra_kwargs = {
            'password': {'write_only': True
                         }
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email= validated_data["email"],
            username= validated_data["username"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            national_code = validated_data["national_code"],
            password = validated_data["password"]
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "first_name", "last_name", "is_registered", "national_code"]
        
      