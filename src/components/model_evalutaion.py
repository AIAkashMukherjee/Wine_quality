from src.config.configuration import ModelEvaluationConfig
import pandas as pd
from sklearn.metrics import accuracy_score,f1_score,precision_score
from src.utils.utlis import save_json
from pathlib import Path
import numpy as np
import joblib


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        acc = np.sqrt(accuracy_score(actual, pred))
        f1 = f1_score(actual, pred, average='macro')
        precision = precision_score(actual, pred, average='macro')

        return acc,f1,precision
    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)

        (acc, f1, precision) = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"Accuracy": acc, "F1_score": f1, "Precision": precision}
        save_json(path=Path(self.config.metric_file_name), data=scores)
