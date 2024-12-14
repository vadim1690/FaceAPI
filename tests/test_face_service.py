import pytest
from src.services.face_service import FaceService
from io import BytesIO
from PIL import Image

def create_mock_image():
    """Creates a mock image for testing."""
    img = Image.new("RGB", (100, 100), color="white")
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return buffer

def test_handle_face_detection():
    mock_file = create_mock_image()
    with pytest.raises(ValueError, match="Uploaded file is not an image."):
        FaceService.handle_face_detection(None)  # Invalid file

    # Simulate a valid file upload
    base64_faces = FaceService.handle_face_detection(mock_file)
    assert isinstance(base64_faces, list)

def test_handle_face_embeddings():
    mock_file = create_mock_image()
    with pytest.raises(ValueError, match="Uploaded file is not an image."):
        FaceService.handle_face_embeddings(None)  # Invalid file

    # Simulate a valid file upload
    embeddings = FaceService.handle_face_embeddings(mock_file)
    assert isinstance(embeddings, list)
