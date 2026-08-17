from rest_framework import serializers
from ...models import School

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