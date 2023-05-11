from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    
    return render_template('index.html') 

@app.route('/plot', methods=['GET','POST'])
def plot_graph():
    df1 = pd.read_csv("csv/Time_feature_matrix_Bearing_1_Test_2.csv",index_col='Unnamed: 0')
    df2 = pd.read_csv("csv/Time_feature_matrix_Bearing_2_Test_2.csv",index_col='Unnamed: 0')
    df3 = pd.read_csv("csv/Time_feature_matrix_Bearing_3_Test_2.csv",index_col='Unnamed: 0')
    df4 = pd.read_csv("csv/Time_feature_matrix_Bearing_4_Test_2.csv",index_col='Unnamed: 0')

    df1.index = pd.to_datetime(df1.index)

    for i,col in enumerate(df1.columns):  
        
            plt.figure(figsize=(10, 5))
            plt.plot(df1.index,df1[col])
            plt.plot(df1.index,df2[col])
            plt.plot(df1.index,df3[col])
            plt.plot(df1.index,df4[col])

            plt.legend(['bearing-1','bearing-2','bearing-3','bearing-4'])

            plt.xlabel("Date-Time")
            plt.ylabel(col)
            plt.title(col)
            plt.show()
            plt.savefig('my_plot.png')
            return render_template('plot.html')
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        
