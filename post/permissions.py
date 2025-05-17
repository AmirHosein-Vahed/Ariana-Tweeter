from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTPermission(BasePermission):
    """
    Custom permission class to handle JWT token authentication
    """
    
    def has_permission(self, request, view):
        try:
            # Get the JWT authentication instance
            jwt_auth = JWTAuthentication()
            
            # Authenticate the request
            user_auth_tuple = jwt_auth.authenticate(request)
            
            if user_auth_tuple is None:
                return False
                
            # Extract user from the auth tuple
            user, token = user_auth_tuple
            
            # Set authenticated user to the request
            request.user = user
            
            # Check if user is authenticated and active
            return bool(user and user.is_authenticated and user.is_active)
            
        except (InvalidToken, TokenError):
            return False
