def load_dataframe(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def calculate_average_purchases(df: pd.DataFrame) -> float:
    return df['purchases'].mean()

def filter_dataframe(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    return df[df[column] == value]

def sort_dataframe(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return df.sort_values(by=column)