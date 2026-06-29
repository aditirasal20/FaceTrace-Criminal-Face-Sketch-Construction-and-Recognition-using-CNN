import firebase_admin
from firebase_admin import credentials, auth

# Initialize only once
if not firebase_admin._apps:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)


def verify_token(id_token):
    """Verify Firebase ID token sent from frontend. Returns uid if valid, None if not."""
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded['uid']
    except Exception as e:
        print(f'[Firebase Auth] Token verification failed: {e}')
        return None


def get_user(uid):
    """Get Firebase user record by UID."""
    try:
        return auth.get_user(uid)
    except Exception as e:
        print(f'[Firebase Auth] Get user failed: {e}')
        return None


def delete_user(uid):
    """Delete a Firebase user by UID."""
    try:
        auth.delete_user(uid)
        print(f'[Firebase Auth] Deleted user: {uid}')
    except Exception as e:
        print(f'[Firebase Auth] Delete user failed: {e}')
