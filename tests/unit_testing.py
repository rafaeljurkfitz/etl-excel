"""Tests for unit functionalities."""

import pandas as pd

from app.pipeline.transform import concat_data_frames

# from app.pipeline import extract_excel, load_em_um_novo_excel, concat_data_frames

# Sample data for testing
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': ['d', 'e', 'f']})


def test_the_concat_of_list_of_data_frames():
    """Test the concat of dataframes."""
    arrange = pd.concat([df1, df2], ignore_index=True)

    act = concat_data_frames([df1, df2])

    assert arrange.equals(act)
