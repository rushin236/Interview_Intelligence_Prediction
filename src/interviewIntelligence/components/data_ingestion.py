import os
import urllib.request as requests
import zipfile

from interviewIntelligence.entity import DataIngestionConfig
from interviewIntelligence.logging import logger
from interviewIntelligence.utils.common import create_directries


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            create_directries([self.config.root_dir])

            if not os.path.exists(self.config.local_data_file):
                file_name, header = requests.urlretrieve(
                    self.config.source_URL, self.config.local_data_file
                )
                logger.info(f"{file_name} downloaded with following info {header}.")
            else:
                logger.info("File already exists")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e:
            raise e
