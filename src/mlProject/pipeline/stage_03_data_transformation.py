from mlProject import logger
from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation

STAGE_NAME = 'Data Transformation'


class DataTransformationPipleline:
    def __init__(self):
        pass

    def main(self):
        
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} Started')
        pipeline = DataTransformationPipleline()
        pipeline.main()
        logger.info(f'{STAGE_NAME} Completed')
    except Exception as e:
        logger.error(f'{STAGE_NAME} Failed')
        logger.error(str(e))
        raise e