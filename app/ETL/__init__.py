"""Esse módulo init contem todas as funções do ETL."""

from .extract import extract_from_excel
from .load import load_excel
from .pipeline import pipeline_completa
from .transform import concat_data_frames
