from rest_framework import serializers
from .models import Student


class StudentSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rool = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.rool = validated_data.get('rool',instance.rool)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #Field lavel validation
    def validate_rool(self, value):
        if value >= 450:
            raise serializers.ValidationError('Seat Fill up')
        return value