"""Modulo com todas as funções de extração de dados."""

import glob  # ? biblioteca para listar arquivos em um diretório
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Ler todos arquivos da pasta ```data/input``` e retorna uma lista de dataframes.

    Args:
        input_path (str): Caminho da pasta onde estão os arquivos Excel.

    Returns:
        list: Lista de dataframes.
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))
    if not all_files:
        raise ValueError('No Excel files found in the specified folder')

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
