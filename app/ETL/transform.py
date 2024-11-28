"""Modulo com todas as funções de transformação de dados."""

from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Concatena uma lista de dataframes em um único dataframe.

    Args:
        data_frame_list (List[pd.DataFrame]): Lista de dataframes

    Returns:
        pd.DataFrame: Um dataframe
    """
    if not data_frame_list:
        raise ValueError('No data to transform')
    return pd.concat(data_frame_list, ignore_index=True)
