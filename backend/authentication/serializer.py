from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all)])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user