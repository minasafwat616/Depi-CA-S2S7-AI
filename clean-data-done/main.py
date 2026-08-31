from preprocessing import *
import pandas as pd
from config import cols_to_drop

def main():
    file_path = input("enter the dataset path : ")
    df = read_file(file_path)
    if df is None:
        return
    print("\nDataset loaded successfully.")
    # Remove unnecessary features 
    df = Drop_unnecessary_features(df, cols_to_drop)
    print("\nUnnecessary features removed.")

    check = input( "\nDo you want to check the data types?"
    " (y/n): " )

    if check.lower() == "y":
        report = check_data_type(df)
        print("\nData Quality Report:")
        print(report)

if __name__ == "__main__":
    main()