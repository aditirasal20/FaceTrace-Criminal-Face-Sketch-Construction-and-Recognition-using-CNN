# precompute_embeddings.py
# Run this file ONCE every time you add new photos to static/photos/
# It saves all photo embeddings to a file so the app doesn't recompute them

import pickle
import os
from cnn_model import get_embedding

PHOTO_FOLDER = 'static/photos'
EMBEDDINGS_FILE = 'embeddings.pkl'

def precompute():
    embeddings = {}
    photos = os.listdir(PHOTO_FOLDER)
    total = len(photos)

    print(f"Found {total} photos. Processing...")

    for i, filename in enumerate(photos):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        path = os.path.join(PHOTO_FOLDER, filename)
        try:
            print(f"  [{i+1}/{total}] Processing {filename}...")
            embeddings[filename] = get_embedding(path)
        except Exception as e:
            print(f"  Skipping {filename}: {e}")

    with open(EMBEDDINGS_FILE, 'wb') as f:
        pickle.dump(embeddings, f)

    print(f"\nDone! Saved {len(embeddings)} embeddings to {EMBEDDINGS_FILE}")
    print("You only need to run this again when you add new photos.")

if __name__ == "__main__":
    precompute()