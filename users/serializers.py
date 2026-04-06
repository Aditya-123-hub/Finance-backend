from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'created_at', 'updated_at', 'password']
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        role = validated_data.get('role', 'viewer')
        password = validated_data.get('password')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            role=role,
            password=password
        )
        return user
    