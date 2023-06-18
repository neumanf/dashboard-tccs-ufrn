import pandas as pd
import plotly.express as px


def get_number_of_papers_by_advisor(df: pd.DataFrame):
    num_papers_by_advisor = df['nome_orientador'].value_counts().reset_index(name='trabalhos').head(10)

    number_of_papers_by_advisor_graph = px.pie(num_papers_by_advisor, values='trabalhos', names='nome_orientador')

    return number_of_papers_by_advisor_graph