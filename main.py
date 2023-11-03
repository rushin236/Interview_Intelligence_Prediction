from interviewIntelligence.logging import logger
from interviewIntelligence.pipline.stage_01_data_ingestion import DataIngestionPipeline
from interviewIntelligence.pipline.stage_02_data_validation import (
    DataValidationPipeline,
)

STAGE_NAME = "data ingestion"
try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
    raise e

STAGE_NAME = "data validation"
try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
    raise e
