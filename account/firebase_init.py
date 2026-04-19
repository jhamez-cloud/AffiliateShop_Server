'''Documentation String'''
from pathlib import Path
import firebase_admin
from firebase_admin import credentials

BASE_DIR = Path(__file__).resolve().parent.parent
cred_path = BASE_DIR / "affiliateshop-ffc2f-firebase-adminsdk-fbsvc-2cc7816070.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    print("🔥 Firebase initialized")
