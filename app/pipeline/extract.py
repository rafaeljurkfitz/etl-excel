import glob  # library to list files
import os  # library to manipulate files and folders
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    A function to read the files of a folder ```data/input``` and return a list of
    dataframes

    args: input_path (str): path to folder with the files

    return: list: list of dataframes
    """

    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
