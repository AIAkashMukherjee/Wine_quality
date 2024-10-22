from src.utils.utlis import read_yaml,create_dir
from src.constants import *
from dataclasses import dataclass
from pathlib import Path
import urllib.request as request
import zipfile
from src.logger.custom_logging import logger
from src.utils.utlis import get_size
from src.entity.config_entity import DataIngestionConfig
import os
import ssl


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config

    def download_file(self):
        # Create an unverified SSL context
        context = ssl._create_unverified_context()

        # Check if file already exists
        if not os.path.exists(self.config.local_data_file):
            # Open the URL with the custom SSL context
            with request.urlopen(self.config.source_URL, context=context) as response:
                with open(self.config.local_data_file, 'wb') as out_file:
                    out_file.write(response.read())
            
            logger.info(f"{self.config.local_data_file} downloaded successfully!")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")  

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) 



