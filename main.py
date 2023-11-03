from interviewIntelligence.logging import logger
from interviewIntelligence.pipline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "data ingestion"
try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
except Exception as e:
    raise e
