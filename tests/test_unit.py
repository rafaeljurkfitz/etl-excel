"""Testes de unitários."""

import os
import subprocess

import pandas as pd
import pytest

from app.ETL import concat_data_frames, extract_from_excel, load_excel

# from app.pipeline.transform import concat_data_frames


# Sample data for testing
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': ['d', 'e', 'f']})


@pytest.fixture
def mock_input_folder(tmpdir):
    """Fixture para criar uma pasta de entrada simulada com arquivos Excel de
    exemplo para testes."""
    # Criando arquivos Excel de exemplo para testes
    input_folder = tmpdir.mkdir('input_folder')
    df1.to_excel(
        input_folder.join('file1.xlsx'), index=False
    )  # Retirado engine='openpyxl'
    df2.to_excel(
        input_folder.join('file2.xlsx'), index=False
    )  # Retirado engine='openpyxl'
    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    """Fixture para criar uma pasta de saída simulada para testes."""
    return str(tmpdir.mkdir('output_folder'))


def test_extract(mock_input_folder):
    """Teste a extração de dados da pasta de entrada."""
    extracted_data = extract_from_excel(mock_input_folder)
    assert len(extracted_data) == 2  # Expecting two DataFrames
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_files(tmpdir):
    """Testa a funcionalidade de extração com uma pasta de entrada vazia."""
    empty_folder = tmpdir.mkdir('empty_folder')
    with pytest.raises(ValueError, match='No Excel files found'):
        extract_from_excel(str(empty_folder))


def test_transform():
    """Testa a transformação de dados."""
    data = [df1, df2]
    arrange = pd.concat(data, ignore_index=True)
    act = concat_data_frames(data)
    assert arrange.equals(act)
    assert len(act) == 6  # 3 rows from df1 + 3 rows from df2
    assert list(act.columns) == ['A', 'B']


def test_transform_empty_list():
    """Testa a transformação de dados com uma lista vazia."""
    empty_list = []
    with pytest.raises(ValueError, match='No data to transform'):
        concat_data_frames(empty_list)


def test_load_no_permission(tmpdir):
    """Testa a funcionalidade de carregamento com uma pasta de saída protegida."""
    # Supondo que a pasta não tenha permissões de gravação
    protected_folder = tmpdir.mkdir('protected_folder')
    if os.name == 'posix':
        os.chmod(str(protected_folder), 0o444)  # Somente permissões de leitura
    elif os.name == 'nt':  # Windows
        # Comandos específicos do Windows para definir permissões somente leitura
        # Aqui você pode usar o método que mencionei anteriormente ou qualquer outro método que funcione para você
        # Exemplo:
        subprocess.run(
            ['icacls', str(protected_folder), '/deny', 'Todos:(OI)(CI)(F)']
        )
        pass
    df = pd.DataFrame({'A': [1], 'B': ['a']})
    with pytest.raises(PermissionError):
        print(str(protected_folder))
        load_excel(df, str(protected_folder), 'test.xlsx')


def test_load(mock_output_folder):
    """Testa a funcionalidade de carregamento."""
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    output_file_name = 'consolidated.xlsx'
    load_excel(df, mock_output_folder, output_file_name)
    assert os.path.exists(os.path.join(mock_output_folder, output_file_name))

    # Verificar se o arquivo de saída tem o conteúdo esperado
    loaded_df = pd.read_excel(
        os.path.join(mock_output_folder, output_file_name)
    )  # Retirado engine='openpyxl'
    pd.testing.assert_frame_equal(loaded_df, df)
