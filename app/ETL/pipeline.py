"""This module contains functions for the ETL process."""

from loguru import logger

from .extract import extract_from_excel
from .load import load_excel
from .transform import concat_data_frames


@logger.catch
def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extract, Transform and load data from Excel files.

    type: input_folder: strs
    """
    data = extract_from_excel(input_folder)
    logger.debug('Extracted data from Excel files.')
    consolidated_df = concat_data_frames(data)
    logger.debug('Transformed data.')
    load_excel(consolidated_df, output_folder, output_file_name)
    logger.debug('Loaded data into Excel file.')
