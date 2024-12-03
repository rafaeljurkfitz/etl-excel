"""module with all the transformation necessary to consolidate the opening data."""

import errno
import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> None:
    """Receive a dataframe and save as excel.

    Args:
        data_frame (pd.DataFrame): dataframe to be save as excel
        output_path (str): path where the file will be saved
        file_name (str): name of folder to be saved

    Returns:
        None:
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError('`data_frame` must be a pandas DataFrame.')
    if not file_name:
        raise ValueError('`file_name` cannot be empty.')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    try:
        data_frame.to_excel(os.path.join(output_path, file_name), index=False)
        logger.debug('File saved successfully!')
    except PermissionError as e:
        raise PermissionError(
            errno.EACCES, f'Permission denied: {output_path}'
        ) from e
    except Exception as e:
        raise RuntimeError(
            f'Failed to save DataFrame as Excel file: {e}'
        ) from e
