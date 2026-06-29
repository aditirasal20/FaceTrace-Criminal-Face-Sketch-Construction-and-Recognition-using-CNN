# cnn_model.py
import numpy as np
import cv2
import os
import pickle
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity

EMBEDDINGS_FILE = 'embeddings.pkl'

# ── Load VGG16 once when app starts ──
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model = Model(inputs=base_model.input, outputs=base_model.output)
print("CNN model loaded!")

# ── Load pre-computed photo embeddings once at startup ──
# Instead of computing them every request, we load the saved file
if os.path.exists(EMBEDDINGS_FILE):
    with open(EMBEDDINGS_FILE, 'rb') as f:
        PHOTO_EMBEDDINGS = pickle.load(f)
    print(f"Loaded {len(PHOTO_EMBEDDINGS)} pre-computed embeddings!")
else:
    PHOTO_EMBEDDINGS = {}
    print("WARNING: No embeddings.pkl found. Run precompute_embeddings.py first!")


def preprocess_for_cnn(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image: {image_path}")
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img.astype('float32'))
    return img


def get_embedding(image_path):
    img = preprocess_for_cnn(image_path)
    features = model.predict(img, verbose=0)
    return features.flatten()


def find_best_match(sketch_path, photo_folder=None):
    """
    Now uses pre-loaded embeddings instead of reprocessing
    every photo from scratch — much faster!
    """
    if len(PHOTO_EMBEDDINGS) == 0:
        print("No embeddings loaded. Run precompute_embeddings.py first!")
        return None, 0.0

    # Only the sketch gets processed through CNN — photos are already done
    sketch_embedding = get_embedding(sketch_path).reshape(1, -1)

    best_match_filename = None
    best_score = -1

    for filename, photo_embedding in PHOTO_EMBEDDINGS.items():
        score = cosine_similarity(
            sketch_embedding,
            photo_embedding.reshape(1, -1)
        )[0][0]

        if score > best_score:
            best_score = score
            best_match_filename = filename

    print(f"Best match: {best_match_filename} | Score: {best_score:.4f}")
    return best_match_filename, round(float(best_score), 4)