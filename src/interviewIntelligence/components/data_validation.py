import os

from interviewIntelligence.entity import DataValidationConfig
from interviewIntelligence.logging import logger
from interviewIntelligence.utils.common import create_directries


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate(self):
        try:
            create_directries([self.config.root_dir])
            valid_dirs = self.config.valid_dirs
            dir_list = os.listdir(self.config.validation_dir)
            dir_list.remove("data.zip")

            status: bool = True
            # print(valid_dirs, dir_list)

            if sorted(valid_dirs) == sorted(dir_list):
                with open(self.config.status_file_path, "w") as f:
                    f.write(f"Validation Status: {status}")
                    logger.info(f"Validation Status: {status}")

            else:
                with open(self.config.status_file_path, "w") as f:
                    f.write(f"Validation Status: { not status}")
                    logger.info(f"Validation Status: { not status}")

        except Exception as e:
            raise e
