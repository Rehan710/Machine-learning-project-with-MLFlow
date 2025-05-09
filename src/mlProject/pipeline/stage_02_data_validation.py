from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config= data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed")
        logger.error(str(e))
        raise e