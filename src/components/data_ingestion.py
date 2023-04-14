import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  ## dataclassess is being useed when we just want to initialize variables not want to initialize any methods

from src.components.data_transformation import DataTransformation

## Initialize the data ingestion configuration
@dataclass
class DataIngestionconfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


## Create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.IngestionConfig = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion methods starts")
        try:

            df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv'))
            logging.info("Dataset read from pandas dataframe")

            # Creating the raw.csv file path and the file itself
            os.makedirs(os.path.dirname(self.IngestionConfig.raw_data_path), exist_ok=True)   ## exist_ok = True is being used becuase if any present directory will be there then the directory will not be created
            df.to_csv(self.IngestionConfig.raw_data_path, index=False)
            
            logging.info('Train-Test split')
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            ## Splitting train and test data
            train_set.to_csv(self.IngestionConfig.train_data_path, index=False, header=True)
            test_set.to_csv(self.IngestionConfig.test_data_path, index=False, header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.IngestionConfig.train_data_path,
                self.IngestionConfig.test_data_path
            )


        except Exception as e:
            logging.info("Exception occured at Data ingestion stage")
            raise CustomException (e,sys)



