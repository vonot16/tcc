import pandas as pd
from glob import glob
from os import getcwd, walk

cwd = getcwd()
original_dataset_dir = f"{cwd}\original_dataset\\"
clean_dataset_dir = f"{cwd}\clean_dataset\\"
datasets_name = []

for (path, folders, files) in walk(original_dataset_dir):
    datasets_name = files

datasets_name.remove('put_datasets_here.txt')

for dataset in datasets_name:
    df = pd.read_csv(f"{original_dataset_dir}{dataset}", sep=',', header=0, index_col=None)
    df.dropna(axis='index', how='any', inplace=True)

    df.to_csv(f"{clean_dataset_dir}{dataset}", sep=',', index=False)