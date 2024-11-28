"""Testes de integração"""
import os
import tempfile

import pandas as pd

from app.ETL import pipeline_completa


def test_integration():
    """
    Teste de integração para verificar a funcionalidade completa de consolidate_excels.

    Esse teste simula um cenário do mundo real criando um diretório temporário
    com um arquivo Excel de exemplo. O teste então verifica se a função de consolidação
    funciona conforme o esperado.
    """
    # Criar uma pasta temporária para simular o ambiente real
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Configurar as pastas de entrada e saída
        input_folder = os.path.join(tmpdirname, 'input')
        output_folder = os.path.join(tmpdirname, 'output')
        os.makedirs(input_folder)

        # Criar um arquivo Excel real para teste
        sample_data = pd.DataFrame(
            {'A': list(range(1, 11)), 'B': list('abcdefghij')}
        )
        sample_file_path = os.path.join(input_folder, 'sample.xlsx')
        sample_data.to_excel(sample_file_path, index=False)

        # Executar a função consolidate_excels
        pipeline_completa(input_folder, output_folder, 'consolidated.xlsx')

        # Verificar se o arquivo de saída existe e tem o conteúdo esperado
        output_file_path = os.path.join(output_folder, 'consolidated.xlsx')
        assert os.path.exists(output_file_path)

        loaded_data = pd.read_excel(output_file_path)
        pd.testing.assert_frame_equal(loaded_data, sample_data)
