"""Esse módulo contém a função pipeline_completa que executa o processo ETL completo."""

from .extract import extract_from_excel
from .load import load_excel
from .transform import concat_data_frames


def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: extrai, transforma e carrega dados de arquivos Excel.

    type: input_folder: strs
    """
    data = extract_from_excel(input_folder)
    consolidated_df = concat_data_frames(data)
    load_excel(consolidated_df, output_folder, output_file_name)
