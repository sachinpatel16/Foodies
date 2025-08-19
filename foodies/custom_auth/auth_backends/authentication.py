from rest_framework.authentication import TokenAuthentication

from foodies.custom_auth.models import MultiToken


class MultiTokenAuthentication(TokenAuthentication):
    model = MultiToken
