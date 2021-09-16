import pandas as pd


def get_signal_from_csv(csv_file):
    emg = pd.read_csv(csv_file, sep='\n', names=['signal'], header=None, index_col=False)
    return emg['signal'].tolist()


