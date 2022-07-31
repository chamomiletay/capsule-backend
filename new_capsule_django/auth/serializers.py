from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.forms import ValidationError
from django.contrib.auth.password_validation import validate_password


#---- define user model ----
User = get_user_model()

class AuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def createAcct(self, validated_data):
        try: verify_password = settings.PASSWORD_VALIDATION_ON
        except: verify_password = False

        if verify_password:
            try: validate_password(validated_data['password'])
            except Exception as e:
                raise serializers.ValidationError(
                    {'password_validation': e.messages}
                )

    #----- authenticated user parameters -----
        authUser = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return authUser

    class Meta:
        model = User
        fields = ('id','username','password','email')