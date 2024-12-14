import face_recognition
import numpy as np
from PIL import Image

def detect_and_crop_faces(file) -> list:
    """
    Detects faces in the photo and crops them.
    :return: List of cropped face images (PIL Images)
    """
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        raise ValueError("No faces detected in the photo.")

    pil_image = Image.open(file)
    cropped_faces = []
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cropped_face = pil_image.crop((left, top, right, bottom))
        cropped_faces.append(cropped_face)

    return cropped_faces

def generate_face_embedding(cropped_face):
    """
    Generate a 128-dimensional face embedding from a cropped face image.
    :param cropped_face: Cropped face as a PIL Image
    :return: 128-dimensional numpy array
    """
    face_array = np.array(cropped_face)
    face_encodings = face_recognition.face_encodings(face_array)
    if not face_encodings:
        raise ValueError("No face encoding could be generated for the input face.")

    return face_encodings[0].tolist()  # convert numpy to list for JSON serialization
