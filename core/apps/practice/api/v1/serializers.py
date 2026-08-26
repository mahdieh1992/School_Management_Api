from rest_framework import serializers
from ...models import Practice, PracticeAnswer
from ....school.models import ClassRoom

class PracticeSerializer(serializers.ModelSerializer):
    class_room = serializers.SlugRelatedField(queryset= ClassRoom.objects.none(), slug_field="name")
    created_by = serializers.SlugRelatedField(read_only=True, slug_field="email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            self.fields["class_room"].queryset = ClassRoom.objects.filter(teacher = request.user)
    
    class Meta:
        model = Practice
        fields = ["id", "title", "body", "deadline", "attachment", "created_by", "class_room"]