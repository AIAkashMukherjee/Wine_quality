

from src.components.model_trainer import ModelTrainer
from src.config.configuration import ConfigManager
from src.logger.custom_logging import logger

STAGE_NAME = "Model Trainer stage"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_trainer_config = config.model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e