from pydantic import BaseModel
from typing import Optional
# Importamos libreria para enumerar modelos
from enum import Enum

class ModelClassifier(str, Enum):
    classiffier_logReg = "logisticRegression_model_more_data_trained"
    classiffier_cat = "cat_model_less_data_trained"