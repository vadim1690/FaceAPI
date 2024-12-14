import logging
from .config import settings

LOG_LEVEL = settings.LOG_LEVEL.upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(settings.APP_NAME)
