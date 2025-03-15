from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.error(f"Failed to execute {STAGE_NAME} pipeline")
        logger.error(str(e))
        raise e