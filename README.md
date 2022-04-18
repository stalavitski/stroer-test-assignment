# Installation

To build and run project run following command:
```
docker-compose up --build
```

# Setup


1. Create a superuser to access admin:
```
docker exec -it stroer-test-assignment python3 manage.py createsuperuser
```

2. Login in admin and create a new application using following instruction
- https://github.com/wagnerdelima/drf-social-oauth2#setting-up-a-new-application

3. In config update following values with corresponding values obtained from Google:
```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = <your app id goes here>
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = <your app secret goes here>
```
To get ID (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY) and secret (SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET): 
- https://console.developers.google.com/apis/credentials 

# Usage

Swagger is accessible at `/swagger/`

`users` endpoints requires authentication. 
Authentication is available at `/auth/convert-token/`.

For the test purposes it's possible to obtain access token from https://developers.google.com/oauthplayground/

Request body example:
```
{
  "backend": "google-oauth2",
  "grant_type": "convert_token",
  "client_id": "client_id_from_application_created_in_django_admin",
  "client_secret": "client_secret_from_application_created_in_django_admin",
  "token": "token_obtained_from_google"
}
```

Response example:
```
{
  "access_token": "access_token",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "refresh_token"
}
```

Use `access_token` value from data above together with `Bearer ` prefix for authentication.

# Testing

To run test, execute following command:
```
docker exec -it stroer-test-assignment python3 manage.py test
```