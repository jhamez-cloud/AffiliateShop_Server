'''Documentation String'''
from pathlib import Path
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from user.models import UserProfile

BASE_DIR = Path(__file__).resolve().parent.parent
cred_path = BASE_DIR / "affiliateshop-ffc2f-firebase-adminsdk-fbsvc-2cc7816070.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    #print("🔥 Firebase initialized (auth)")


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
