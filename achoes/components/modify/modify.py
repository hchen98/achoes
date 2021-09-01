import pandas as pd

def changeType(df, types):
    '''
    Change data type of columns in a dataframe.
    types: dict of column names and data types
    '''

    for i in types:
        df[i[0]] = df[i[0]].astype(i[1])

    return df