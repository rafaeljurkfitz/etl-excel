"""This module contains functions for the ETL process."""

from .extract import extract_from_excel
from .load import load_excel
from .transform import concat_data_frames


def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extract, Transform and load data from Excel files.

    type: input_folder: strs
    """
    data = extract_from_excel(input_folder)
    print('Extracted data from Excel files.')
    consolidated_df = concat_data_frames(data)
    print('Transformed data.')
    load_excel(consolidated_df, output_folder, output_file_name)
    print('Loaded data into Excel file.')
