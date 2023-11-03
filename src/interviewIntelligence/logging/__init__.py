import logging
import os
import sys

dir = "logs"
logging_str = "[%(asctime)s]: %(levelname)s %(module)s %(message)s"
file_path = os.path.join(dir, "running_logs.log")
os.makedirs(dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(file_path), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("interviewIntelligence")
