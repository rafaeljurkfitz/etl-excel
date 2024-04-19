from pipeline import extract

path = "data/input"

list_of_data_frame = extract.extract_from_excel(path)
print(list_of_data_frame)