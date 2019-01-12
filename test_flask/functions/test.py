import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./baseball-test-d74f9-firebase-adminsdk-hr1ju-0361bcfbec.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('users').get()
for doc in docs:
    print(doc.to_dict())