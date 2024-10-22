from src.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_columns(self):
        try:
            val_Status=True

            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)

            all_schema=self.config.all_schema.keys()


            for col in all_cols:
                if col not in all_schema:
                    val_Status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {val_Status}")
                else:
                    val_Status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {val_Status}")


            return val_Status

        except Exception as e:
            raise e