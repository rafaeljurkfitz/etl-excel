"""main project pipeline."""

from ETL import pipeline_completa
from loguru import logger


def consolidate_files():
    """Consolidates the gerated Excel files into a single file."""
    input_folder = 'data/input'
    output_folder = 'data/output'
    output_file_name = 'consolidated_absenteeism_data.xlsx'
    logger.add('./logs/file_{time}.log', rotation='10 MB')
    pipeline_completa(input_folder, output_folder, output_file_name)


if __name__ == '__main__':
    consolidate_files()
