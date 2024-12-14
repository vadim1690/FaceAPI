from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.responses import StreamingResponse

from src.models.requests import Base64Request
from src.models.responses import CroppedFaceResponse, FaceEmbeddingResponse
from src.services.face_service import FaceService

router = APIRouter()

@router.post("/detect-faces", response_model=CroppedFaceResponse)
async def detect_faces(file: UploadFile = File(...)):
    """
    Endpoint that accepts a photo upload, detects faces, and returns cropped face images as base64.
    """
    try:
        # Delegate to the service layer
        base64_faces = FaceService.handle_face_detection(file)
        return CroppedFaceResponse(faces=base64_faces)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/face-embeddings", response_model=FaceEmbeddingResponse)
async def face_embeddings(file: UploadFile = File(...)):
    """
    Endpoint that accepts a photo upload, detects faces, and generates embeddings.
    """
    try:
        # Delegate to the service layer
        embeddings = FaceService.handle_face_embeddings(file)
        return FaceEmbeddingResponse(embeddings=embeddings)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/detect-faces-base64", response_model=CroppedFaceResponse)
async def detect_faces_base64(request: Base64Request):
    """
    Endpoint that accepts a base64 image, detects faces, and returns cropped face images as base64.
    """
    try:
        # Delegate to the service layer
        base64_faces = FaceService.handle_face_detection_base64(request.base64_image)
        return CroppedFaceResponse(faces=base64_faces)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/face-embeddings-base64", response_model=FaceEmbeddingResponse)
async def face_embeddings_base64(request: Base64Request):
    """
    Endpoint that accepts a base64 image, detects faces, and generates embeddings.
    """
    try:
        # Delegate to the service layer
        embeddings = FaceService.handle_face_embeddings_base64(request.base64_image)
        return FaceEmbeddingResponse(embeddings=embeddings)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/detect-faces-return-file")
async def detect_faces_return_file(file: UploadFile = File(...)):
    """
    Endpoint that accepts a photo upload, detects faces, and returns cropped faces as file bytes.
    """
    try:
        # Delegate to the service layer
        file_bytes = FaceService.handle_face_detection_return_file(file)


        # Return the file as a StreamingResponse
        return StreamingResponse(file_bytes, media_type="image/jpeg", headers={
            "Content-Disposition": "attachment; filename=cropped_faces.jpg"
        })
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")