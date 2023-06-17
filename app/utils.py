import pandas as pd

def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(inplace=False)

    # As it has many inconsistent dates, it was necessary to remove the column so as not to affect the analyses
    df = df.drop('data_defesa', axis=1)

    df = df[(df['ano'] > 1900) & (df['ano'] < 2050)]

    df['ano'] = df['ano'].astype(str)
    df['ano'] = df['ano'].str.split('.').str[0]

    return df