from rest_framework.authentication import BaseAuthentication

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return None