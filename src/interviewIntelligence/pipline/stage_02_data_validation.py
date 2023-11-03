from interviewIntelligence.components.data_validation import DataValidation
from interviewIntelligence.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate()
        except Exception as e:
            raise e
