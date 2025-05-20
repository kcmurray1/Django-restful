# this project is used to learn about Authentication and Authorization in Django 



# Django automatically makes the table "auth_user"


# Hash function
It is important not to store the passsword as plaintext in the DB

Thus we can use a one-way hash function

hash(username + password) -> passworld field in DB
# Authenticate
check if hash(username + password) == password field in DB
# Authenticate with Salt
check if hash(username + password + salt) == passworld field in DB

## **Do not** use Create when saving passwords
Django has built in password obscuring for the built in Users table

**Do not** add Users with create
```
john = User.objects.create(username="john", password="johnpwd1", email='john@abc.com')
```
add Users with create_user
```
john = User.objects.create_user(username="john", password="johnpwd1", email='john@abc.com')
```

# Enabling AUthentication in Django
Go to settings.py 
add the code to specify the authentication method
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' :
    (
        'rest_framework.authentication.BasicAuthentication',
    )
}
```
Then go to views.py to add the Authentication permission inside the view class
```
  permission_classes = [
        permissions.IsAuthenticated,
    ]
```

## NOTE
This basic authentication requires credentials to be passed in every request which can be unsafe and inconvienient for the user


# Authentication method 2: token
Install another 3rd party package where jwt = JSON web token
```
pip install djangorestframework-simplejwt
```
Then update installed apps in settings.py
```
'rest_framework_simplejwt'
```
Then update REST_FRAMEWORK in settings.py
```
"rest_framework_simplejwt.authentication.JWTAuthentication"
```
This added package allows the user to access the Token we want shared between the server and user

Update installed apps in settings.py to include 'rest_framework.authtoken'

Then migrate the app to apply the changes to settings.py
```
python manage.py migrate
```

Manually Create a token
```
john = User.objects.get(username='john')
token = Token.objects.create(user=john)
print(token.key)
```

## Verifying signature during development
You can send a post request to an established view like http://127.0.0.1:8000/api/token

This will require credentials like username and password and will respond with a token. This token can be pasted into the JWT debugger https://jwt.io/ This will display information in the token, like the expiration and creation time.

## Token Expiration
By default the token will have a 5 minute lifespan. Machines typically automatically refresh tokens; thus, users do not have to actively manage it themselves. Having an tokens that expire acts as a security measure so, if a threat actor manages to take the token, it will hopefully be expired and unusable.

## Performance
JWT does not take up space, it uses an in-memory check to verify the user.
Additionally there is no table lookup which makes it both storage and computationally performant.
