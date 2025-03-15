import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTansformationConfig


class DataTransformation:
    def __init__(self, config:DataTansformationConfig):
        self.config = config

    def train_test_split(self):
        logger.info(f"Train test split")

        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
