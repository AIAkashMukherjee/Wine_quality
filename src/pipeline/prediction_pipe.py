import joblib 
from pathlib import Path


class PredicitonPipe:
    def __init__(self):
        self.model=joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self,X):
        prediction=self.model.predict(X)

        return prediction    