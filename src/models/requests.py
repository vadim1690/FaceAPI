# Base64 request models
from pydantic import BaseModel

class Base64Request(BaseModel):
    base64_image: str