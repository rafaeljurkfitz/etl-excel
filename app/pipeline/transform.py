from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function to transform a list of dataframes in only one dataframe
    """

    return pd.concat(data_frame_list, ignore_index=True)
