# handling csv format file data
import pandas as pd

global df

def pre_read_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df