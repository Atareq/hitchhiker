from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed



def get_user_pk_from_token(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if not auth_header:
        raise AuthenticationFailed("Authorization header missing")

    # Extract the token part (e.g., "Bearer <token>")
    token = auth_header.split(' ')[1]

    access_token_obj = AccessToken(token)
    user_pk = access_token_obj['user_id']
    return user_pk