import glob
import os
import pandas as pd


def read_data_from_csv_into_one_dataframe(CSV_source):
    all_files = glob.glob(os.path.join(CSV_source, "*.csv"))
    dataframes = (pd.read_csv(f) for f in all_files)
    big_dataframe = pd.concat(dataframes, ignore_index=True)
    return big_dataframe


path = '/home/magdalena/Desktop/Ardigen'
print read_data_from_csv_into_one_dataframe(path)