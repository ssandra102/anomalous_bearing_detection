
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
import os
from exceptions import CustomException


class handler:
    def __init__(self):
          pass
    
    def compute_skewness(self,x):
    
        n = len(x)
        third_moment = np.sum((x - np.mean(x))**3) / n
        s_3 = np.std(x, ddof = 1) ** 3
        return third_moment/s_3

    def compute_kurtosis(self,x):    
        n = len(x)
        fourth_moment = np.sum((x - np.mean(x))**4) / n
        s_4 = np.std(x, ddof = 1) ** 4
        return fourth_moment / s_4 - 3
    
    def transformation(self,path,test_no):
        for bearing_no in [1,2,3,4]:
            Time_feature_matrix=pd.DataFrame()
            
            for filename in os.listdir(path):
            
                dataset=pd.read_csv(os.path.join(path, filename), sep='\t',header=None)

                bearing_data = np.array(dataset.iloc[:,bearing_no-1])

                feature_matrix=np.zeros((1,9))
                temp = bearing_data
                feature_matrix[0,0] = np.max(temp)
                feature_matrix[0,1] = np.min(temp)
                feature_matrix[0,2] = np.mean(temp)
                feature_matrix[0,3] = np.std(temp, ddof = 1)
                feature_matrix[0,4] = np.sqrt(np.mean(temp ** 2))
                feature_matrix[0,5] = self.compute_skewness(temp)
                feature_matrix[0,6] = self.compute_kurtosis(temp)
                feature_matrix[0,7] = feature_matrix[0,0]/feature_matrix[0,4]
                feature_matrix[0,8] = feature_matrix[0,4]/feature_matrix[0,2]

                df = pd.DataFrame(feature_matrix)
                df.index=[filename[:-3]]

                Time_feature_matrix = pd.concat([df, Time_feature_matrix])

            try:
                # Time_feature_matrix
                Time_feature_matrix.columns = ['Max','Min','Mean','Std','RMS','Skewness','Kurtosis','Crest Factor','Form Factor']
                Time_feature_matrix.index = pd.to_datetime(Time_feature_matrix.index, format='%Y.%m.%d.%H.%M')

                Time_feature_matrix = Time_feature_matrix.sort_index()

                Time_feature_matrix.to_csv("Time_feature_matrix_Bearing_{}_Test_{}.csv".format(bearing_no,test_no))
            except Exception as e:
                    raise CustomException(e,sys)
