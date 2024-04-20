"""module for extracting the necessary data to consolidate opening data."""

import glob  # library to list files
import os  # library to manipulate files and folders
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Read the files of a folder ```data/input``` and return a list of dataframes.

    Args:
        input_path (str): Path to folder with the files

    Returns:
        list: list of dataframes
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))
    if not all_files:
        raise ValueError('No Excel files found in the specified folder')

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
