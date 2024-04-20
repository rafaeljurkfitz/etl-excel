"""module with all the transformations necessary to consolidate the opening data."""

from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Transform a list of dataframes in only one dataframe.

    Args:
        data_frame_list (List[pd.DataFrame]): list of dataframes

    Returns:
        pd.DataFrame: one dataframe
    """
    if not data_frame_list:
        raise ValueError('No data to transform')
    return pd.concat(data_frame_list, ignore_index=True)
