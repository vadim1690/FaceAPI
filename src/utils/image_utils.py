import base64
import io
from typing import List
from PIL import Image

def image_to_base64(img: Image.Image) -> str:
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode('utf-8')

def images_to_base64(images: List[Image.Image]) -> List[str]:
    return [image_to_base64(img) for img in images]


def base64_to_image(base64_string):
    """
    Converts a base64 string to a PIL Image.
    """
    image_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_data))

