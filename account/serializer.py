from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token

    def validate(self, attrs):

        email = attrs.get('email') # Get email from the validated data
        password = attrs.get('password') # Get password

        # from django.contrib.auth import authenticate
        from django.contrib.auth import get_user_model

        User = get_user_model()

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("No active account found with the given credentials.")

            if not user.check_password(password):
                 raise serializers.ValidationError("No active account found with the given credentials.")

            if not user.is_active:
                 raise serializers.ValidationError("This account has been disabled.")

            self.user = user

        else:
            # If email or password were not provided
            raise serializers.ValidationError('Must include "email" and "password".')

        data = super().validate(attrs) # This will now use self.user to generate tokens

        # You might want to remove the password from the validated data before returning
        if 'password' in data:
            del data['password']

        return data