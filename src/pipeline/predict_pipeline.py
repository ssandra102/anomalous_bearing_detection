import sys
import pandas as pd
from src.exceptions import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
                 DP1: float,
                 DP2: float,
                 DP3: float,
                 DP4: float):

        self.DP1 = DP1
        self.DP2 = DP2
        self.DP3 = DP3
        self.DP4 = DP4


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "DP1": [self.DP1],
                "DP2": [self.DP2],
                "DP3": [self.DP3],
                "DP4": [self.DP4]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)