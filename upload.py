import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../../JSProjects/VapeToolAdmin/vape-tool-pro-firebase-adminsdk-8mu7u-87260583c3.json")
app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://vape-tool-pro.firebaseio.com'})
print('project ' + app.project_id)

batteries_ref = db.reference('batteries')

