# serializers.py
from rest_framework import serializers
from .models import CustomUser, Content, Category


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, 
                                     error_messages={'min_length': 'Password must be at least 8 characters long.'})
    full_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True, min_length=10, max_length=10)
    pincode = serializers.CharField(required=True, min_length=6, max_length=6)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'full_name', 'phone', 'address', 'city', 'state', 'country', 'pincode']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone=validated_data['phone'],
            address=validated_data.get('address', ''),
            city=validated_data.get('city', ''),
            state=validated_data.get('state', ''),
            country=validated_data.get('country', ''),
            pincode=validated_data['pincode']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'user', 'title', 'body', 'summary', 'document', 'categories']
        read_only_fields = ['user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SearchSerializer(serializers.Serializer):
    search_param = serializers.CharField(max_length=255, required=True)