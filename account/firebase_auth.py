'''Documentation String'''
import os
import json
import base64
from user.models import UserProfile
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from dotenv import load_dotenv
load_dotenv()


if not firebase_admin._apps:
    encoded = os.environ.get("FIREBASE_CREDENTIALS_B64")

    if not encoded:
        raise Exception("Firebase credentials missing")

    decoded = base64.b64decode(encoded).decode("utf-8")
    cred_dict = json.loads(decoded)

    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

    print("🔥 Firebase initialized")

class FirebaseAuthentication(BaseAuthentication):
    '''Documentation String'''
    def authenticate(self, request):
        #print("🔥 FIREBASE AUTH ENTERED")

        header = request.headers.get("Authorization")

        if not header:
            return None

        try:
            token = header.split(" ")[1]
            decoded_token = auth.verify_id_token(token)

            uid = decoded_token["uid"]
            email = decoded_token.get("email")

            user, created = UserProfile.objects.get_or_create( #pylint:disable=e1101
                firebase_uid=uid,
                defaults={"email": email}
            )

           # print("✅ USER:", user, "CREATED:", created)

            return (user, None)

        except Exception as e:
            #print("❌ AUTH ERROR:", e)
            raise AuthenticationFailed("Invalid Firebase token") from e
