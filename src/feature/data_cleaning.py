import pandas as pd


class DataCleaning:
    data = None

    def __init__(self, data=None):
        if data is None:
            raise ValueError('Data must be provided')
        self.data = data

    def _drop_columns(self, df, column):
        df = df.drop([column], axis=1, inplace=True)
        return df

    def change_to_type(self, df, column, new_type):
        df = df.astype({column: new_type})
        return df

    def rename_columns(self, df, old_name, new_name):
        df = df.rename(columns={old_name: new_name})
        return df


if __name__ == '__main__':
    d = DataCleaning()
    DataCleaning.change_to_type()
