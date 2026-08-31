import pandas as pd

def read_file(file_path:str)-> pd.DataFrame|None:
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("The file cannot be read.")

def Drop_unnecessary_features(df:pd.DataFrame, cols_to_drop:list) -> pd.DataFrame :
    df_drop = df.drop(columns = cols_to_drop  )
    return df_drop

def check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({ "Column Name": df.columns,
                            "Data Type": df.dtypes.astype(str),
                            "Unique Values": df.nunique() })
    return result.T


