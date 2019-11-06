from rest_framework import serializers

from .models import Student, Address

# Serializer for Student model
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'code', 'first_name', 'last_name']


# Serializer for Address Model
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'student', 'address_type', 'address']
