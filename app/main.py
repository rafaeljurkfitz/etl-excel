"""main project pipeline."""

from ETL import pipeline_completa


def consolidate_files():
    """Consolidates the gerated Excel files into a single file."""
    input_folder = 'data/input'
    output_folder = 'data/output'
    output_file_name = 'consolidated_absenteeism_data.xlsx'
    pipeline_completa(input_folder, output_folder, output_file_name)


if __name__ == '__main__':
    consolidate_files()
