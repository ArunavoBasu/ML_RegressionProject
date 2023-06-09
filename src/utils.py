import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

##----- Saving the pickle file --------------
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

## --------  Evaluating Model  --------------
def evaluate_model(X_train, y_train, X_test, y_test, models):
    # mae = mean_absolute_error(true, predicted)
    # mse = mean_squared_error(true, predicted)
    # rmse = np.sqrt(mean_squared_error(true, predicted))
    # r2_square = r2_score(true, predicted)
    # return mae, rmse, r2_square
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]

            # Train model
            model.fit(X_train, y_train)

            # Predict test data
            y_pred = model.predict(X_test)

            # Get R2 score for train and test data
            test_model_score = r2_score(y_test, y_pred)

            report[list(models.keys())[i]] =  test_model_score
        
        return report

    except Exception as e:
        logging("Error occured during model training")
        raise CustomException(e,sys)


#------------ To Load the pickle file ------------------
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)