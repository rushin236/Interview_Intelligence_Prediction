import os
from pathlib import Path

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from interviewIntelligence.logging import logger


@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
    """This function reads yaml and returns config box

    Args:
        file_path (Path): yaml file path

    Returns:
        ConfigBox: ConfigBox which can be accessed and dict
    """
    try:
        with open(yaml_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # logger.info(f"Yaml file content loaded successful")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directries(list_of_path: list, verbose: bool = True):
    """This function creates directorise in list

    Args:
        list_of_path (list): list of path
        verbose (bool, optional): for logging. Defaults to True.
    """
    for path in list_of_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
        else:
            logger.info(f"Directory already exists!")
