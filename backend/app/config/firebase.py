import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

# Path to service account key
cred_path = os.path.join(os.path.dirname(__file__), "../../keys/taskflow-ddf5c-firebase-adminsdk-fbsvc-66a50887bb.json")

# Initialize Firebase Admin SDK
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

print("✅ Firebase Admin SDK initialized successfully")