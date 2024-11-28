"""Arquivo main do projeto."""

from ETL import pipeline_completa


def consolidate_files():
    """Função que consolida os arquivos Excel de input em um único arquivo de output."""
    input_folder = 'data/input'
    output_folder = 'data/output'
    output_file_name = 'consolidated_absenteeism_data.xlsx'
    pipeline_completa(input_folder, output_folder, output_file_name)


if __name__ == '__main__':
    consolidate_files()
