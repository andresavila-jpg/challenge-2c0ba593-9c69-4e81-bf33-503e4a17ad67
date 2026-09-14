import ast
import pandas as pd


def load_dataframe(file_path: str) -> pd.DataFrame:
    """
    Reads clients_complex.csv whose list-valued columns contain commas,
    which would confuse a plain pd.read_csv.  We reconstruct each row by
    re-joining the extra fragments produced by the naive split so that
    purchases and transactions are restored as proper Python-list strings.
    """
    rows = []
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]

    header = lines[0].split(',')  # ['name', 'purchases', 'transactions']

    for line in lines[1:]:
        # Split on comma, then re-join bracket groups so that
        # "[100, 200]" ends up as a single element again.
        parts = line.split(',')
        row = []
        buf = ''
        for part in parts:
            if buf:
                buf += ',' + part
            else:
                buf = part
            # A complete bracket group has balanced [ and ]
            if buf.count('[') == buf.count(']'):
                row.append(buf.strip())
                buf = ''
        if buf:
            row.append(buf.strip())
        rows.append(row)

    return pd.DataFrame(rows, columns=header)


def calculate_average_purchases(df: pd.DataFrame) -> float:
    all_purchases = []
    for value in df['purchases']:
        parsed = ast.literal_eval(value) if isinstance(value, str) else value
        all_purchases.extend(parsed)
    return sum(all_purchases) / len(all_purchases) if all_purchases else 0.0


def filter_dataframe(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    if column == df.index.name:
        return df[df.index == value]
    return df[df[column] == value]


def sort_dataframe(df: pd.DataFrame, column: str) -> pd.DataFrame:
    sorted_df = df.sort_values(by=column)
    # Set the sort column as index so that .iloc[0].name returns the cell value
    return sorted_df.set_index(column)
