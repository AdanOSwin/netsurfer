import os

print(os.environ['HOME'])
print(os.environ['USERNAME'])
print(os.environ['AUTH_CODE'])


USERNAME = os.environ['USERNAME']
AUTH_CODE = os.environ['AUTH_CODE']

username = input("INgresar usuario: ")
auth_code = input("Ingresar contraseña: ")

if(username == USERNAME and auth_code == AUTH_CODE):
    print("Access Granted")
else:
    print("Access Denied")