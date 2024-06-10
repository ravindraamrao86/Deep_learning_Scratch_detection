
############# 1st Step for data Ingistion

import os
import sys
from src.components.exception import CustomException
from src.pipline.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("data", "raw", "dataset.csv")
    train_data_path: str = os.path.join("data", "processed", "train.csv")
    test_data_path: str = os.path.join("data", "processed", "test.csv")

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion process")
        try:
            # Example: read a csv file
            df = pd.read_csv(self.config.raw_data_path)
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            train_df.to_csv(self.config.train_data_path, index=False)
            test_df.to_csv(self.config.test_data_path, index=False)

            logging.info("Data ingestion completed successfully")
            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logging.error("Error during data ingestion")
            raise CustomException(e)

