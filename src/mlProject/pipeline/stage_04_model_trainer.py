from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = 'Model Trainer Stage'

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train()


if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} started')
        pipeline = ModelTrainerTrainingPipeline()
        pipeline.main()
        logger.info(f'{STAGE_NAME} completed')
    except Exception as e:
        logger.error(f'{STAGE_NAME} failed: {str(e)}')
        raise e
