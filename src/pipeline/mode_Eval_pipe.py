
from src.components.model_evalutaion import ModelEvaluation
from src.config.configuration import ConfigManager
from src.logger.custom_logging import logger

STAGE_NAME = "Model Evaluation stage"


class ModelEvalPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_evaluation_config = config.model_evluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvalPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e        