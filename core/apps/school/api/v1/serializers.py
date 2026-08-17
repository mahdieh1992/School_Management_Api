from rest_framework import serializers
from ...models import School, Lesson, ClassRoom
from django.contrib.auth import get_user_model

User = get_user_model()

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        
class NearestSchoolSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = ['name', 'latitude', 'longitude', 'distance']
        
    def get_distance(self, obj):
        # Return calculated distance value here
        return getattr(obj, 'distance', 0.0)
    
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        
class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(queryset = User.objects.filter(groups__name = "Teacher"), slug_field="email")
    student = serializers.SlugRelatedField(queryset = User.objects.filter(groups__name = "Student"),many= True, slug_field="email")
    school = serializers.SlugRelatedField(queryset=School.objects.all(),slug_field="name")
    lesson = serializers.SlugRelatedField(queryset=Lesson.objects.all(),slug_field="title")
    class Meta:
        model = ClassRoom
        fields = ['teacher', 'name', 'school', 'lesson', 'student']