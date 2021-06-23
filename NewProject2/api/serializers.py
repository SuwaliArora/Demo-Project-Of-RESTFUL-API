from .models import Student
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)   #new data from user
    roll = serializers.IntegerField()            #new data from user
    city = serializers.CharField(max_length=100)  #new data from user

    # create operation
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):  #instance= data stored in database
        print(instance.name) #previous name
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)  #updated name
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
