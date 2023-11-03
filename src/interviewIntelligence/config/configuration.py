from interviewIntelligence.constants import *
from interviewIntelligence.entity import DataIngestionConfig, DataValidationConfig
from interviewIntelligence.utils.common import create_directries, read_yaml


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directries([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            validation_dir=config.validation_dir,
            valid_dirs=config.valid_dirs,
            status_file_path=config.status_file_path,
        )

        return data_validation_config
