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

# NOTE
This basic authentication requires credentials to be passed in every request which can be unsafe and inconvienient for the user


# Authentication method 2: token
Update installed apps in settings.py to include 'rest_framework.authtoken'

Then migrate the app to apply the changes to settings.py
```
python manage.py migrate
```

Create a token
```
john = User.objects.get(username='john')
token = Token.objects.create(user=john)
print(token.key)
```