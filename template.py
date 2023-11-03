import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")

project_name = "interviewIntelligence"

list_of_path = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipline/__init__.py",
    "research/trails.ipynb",
    "setup.py",
    "params.yaml",
    "config/config.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
]

for path in list_of_path:
    path = Path(path)
    file_dir, file_name = os.path.split(path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating folder: {file_dir} for {file_name}")

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            pass
            logging.info(f"Creating file: {file_name}")

    else:
        logging.info(f"File: {file_name} already exists.")
