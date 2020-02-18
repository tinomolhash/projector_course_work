import os
from typing import List

import joblib
import numpy as np
from sklearn.pipeline import Pipeline


class NewsPredictor:
    def __init__(self, model: Pipeline, target_names: List[str]) -> None:
        self._model = model
        self.target_names = target_names

    @classmethod
    def load(cls, model_folder: str) -> "NewsPredictor":
        model = joblib.load(os.path.join(model_folder, "model.pkl"))
        target_names = joblib.load(os.path.join(model_folder, "target_names.pkl"))
        return cls(model=model, target_names=target_names)

    def predict(self, samples: List[str]) -> List[str]:
        predictions = self._model.predict(samples)
        class_predictions = [self.target_names[target_class_id] for target_class_id in predictions]
        return class_predictions

    def predict_proba(self, samples: List[str]) -> np.array:
        predictions = self._model.predict_proba(samples)
        return predictions
