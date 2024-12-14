from io import BytesIO
from src.services.face_processing import detect_and_crop_faces, generate_face_embedding
from src.utils.image_utils import images_to_base64, base64_to_image


class FaceService:
    @staticmethod
    def handle_face_detection(file):
        """
        Handles the entire logic for face detection from a file.
        Validates the uploaded file, detects faces, and returns base64-encoded cropped faces.
        """
        if not file.content_type.startswith("image/"):
            raise ValueError("Uploaded file is not an image.")

        # Detect and crop faces
        cropped_faces = detect_and_crop_faces(file.file)

        # Convert to base64
        base64_faces = images_to_base64(cropped_faces)
        return base64_faces

    @staticmethod
    def handle_face_embeddings(file):
        """
        Handles the entire logic for generating face embeddings from a file.
        Validates the uploaded file, detects faces, and generates embeddings for each face.
        """
        if not file.content_type.startswith("image/"):
            raise ValueError("Uploaded file is not an image.")

        # Detect and crop faces
        cropped_faces = detect_and_crop_faces(file.file)

        # Generate embeddings
        embeddings = [generate_face_embedding(face) for face in cropped_faces]
        return embeddings

    @staticmethod
    def handle_face_detection_base64(base64_string):
        """
        Handles face detection from a base64 string.
        Decodes the base64 image, detects faces, and returns base64-encoded cropped faces.
        """
        # Decode base64 string to an image
        image = base64_to_image(base64_string)

        # Detect and crop faces
        cropped_faces = detect_and_crop_faces(image)

        # Convert cropped faces to base64
        base64_faces = images_to_base64(cropped_faces)
        return base64_faces

    @staticmethod
    def handle_face_embeddings_base64(base64_string):
        """
        Handles face embeddings generation from a base64 string.
        Decodes the base64 image, detects faces, and generates embeddings for each face.
        """
        # Decode base64 string to an image
        image = base64_to_image(base64_string)

        # Detect and crop faces
        cropped_faces = detect_and_crop_faces(image)

        # Generate embeddings
        embeddings = [generate_face_embedding(face) for face in cropped_faces]
        return embeddings

    @staticmethod
    def handle_face_detection_return_file(file):
        """
        Handles face detection and returns a file containing cropped faces.
        """
        if not file.content_type.startswith("image/"):
            raise ValueError("Uploaded file is not an image.")

        # Detect and crop faces
        cropped_faces = detect_and_crop_faces(file.file)

        # Create an in-memory file
        output = BytesIO()
        for i, face in enumerate(cropped_faces):
            face.save(output, format="JPEG")
        output.seek(0)
        return output
