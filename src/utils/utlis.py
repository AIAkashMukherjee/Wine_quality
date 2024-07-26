import os
from box.exceptions import BoxValueError
from src.logger.custom_logging import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox       
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml)-> ConfigBox:
    '''
    For Config.yaml and schema.yaml
    '''
    try:
        with open (path_to_yaml)as f:
            conetent=yaml.safe_load(f)
            return ConfigBox(conetent)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dir(path_to_dir:list,verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'Dir created {path}') 


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"             