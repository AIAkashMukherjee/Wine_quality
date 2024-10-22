import os
from src.logger.custom_logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.scaler = StandardScaler()

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting_and_scaling(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        # Assuming the features are all columns except the target (last column)
        X_train = train.iloc[:, :-1]
        y_train = train.iloc[:, -1]
        X_test = test.iloc[:, :-1]
        y_test = test.iloc[:, -1]

        # Apply StandardScaler to the features (not target)
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Combine scaled features with the target
        train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        train_scaled['target'] = y_train.values

        test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        test_scaled['target'] = y_test.values

        # Save the scaled train and test sets as CSV files
        train_scaled.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_scaled.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Logging information
        logger.info("Data split into training and test sets")
        logger.info(f"Train shape: {train_scaled.shape}")
        logger.info(f"Test shape: {test_scaled.shape}")

        # Optional: Print the shapes for quick debugging
        print(f"Train shape: {train_scaled.shape}")
        print(f"Test shape: {test_scaled.shape}")