import pyrebase
import json
from pprint import pprint

# get reference to firebase client
config = {
    'apiKey': 'YourAPIKey',
    'authDomain': 'YourAuthDoman.com',
    'databaseURL': 'https://yourdatabse.firebaseio.com',
    'projectId': 'yourprojectID',
    'storageBucket': 'yourdatabase.appspot.com',
    'messagingSenderId': 'YoursenderID'
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in

email = 'yourEmail@gmail/oryahoowhaterver.com'  # Replace Email
password = 'yourPassword'  # Replace Password

user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

### open json file and get ready to import to firebase
with open ("/path/to/data.json",'r') as data_file:
    data=json.load(data_file)
pprint(data)


db.child("").remove()
results = db.child('').set(data, user['idToken'])

#print("finished!! results: ", results)

