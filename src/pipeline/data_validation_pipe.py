
from src.components.data_validation import DataValidation
from src.config.configuration import ConfigManager
from src.logger.custom_logging import logger

STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_val_config=config.get_data_validation_config()
        data_val=DataValidation(config=data_val_config)
        data_val.validate_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e