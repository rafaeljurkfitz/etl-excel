import pandas as pd
import os


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> None:
    
    """
    Receive a dataframe and save as excel

    args:
    data_frame (pd.DataFrame): dataframe to be save as excel
    output_path (str): path where the file will be saved
    file_name (str): name of folder to be saved

    return: None
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    print("File saved successfully!")