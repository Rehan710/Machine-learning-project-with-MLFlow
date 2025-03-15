from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipleline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:  
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataTransformationPipleline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise e


STAGE_NAME = "Model Training stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise e

STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise e