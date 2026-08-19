from rest_framework import serializers
from ...models import News
from ....school.models import ClassRoom
from django.contrib.auth import get_user_model

User = get_user_model()
class NewsSerializer(serializers.ModelSerializer):
    class_room = serializers.SlugRelatedField(queryset= ClassRoom.objects.none(), slug_field="name")
    created_by = serializers.SlugRelatedField(read_only=True, slug_field="email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            self.fields["class_room"].queryset = ClassRoom.objects.filter(teacher = request.user)
    class Meta:
        model = News
        fields = ["title", "body", "class_room","created_by"]
