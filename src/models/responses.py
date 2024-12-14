from pydantic import BaseModel
from typing import List

class CroppedFaceResponse(BaseModel):
    faces: List[str]  # base64 encoded strings

class FaceEmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
