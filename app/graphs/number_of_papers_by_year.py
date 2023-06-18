import pandas as pd
import plotly.express as px


def get_number_of_papers_by_year(df: pd.DataFrame):
    ano_counts = df['ano'].str.split('.').str[0].astype(int).value_counts().sort_index()
    mean_count = ano_counts.mean()

    num_papers_by_course_df = pd.DataFrame({
        "Ano": ano_counts.index,
        "Número de trabalhos": ano_counts.values,
        "Média": mean_count
    })

    number_of_papers_by_year_graph = px.line(num_papers_by_course_df, x="Ano", y="Número de trabalhos")
    number_of_papers_by_year_graph.add_scatter(x=num_papers_by_course_df["Ano"],
                                               y=num_papers_by_course_df["Média"],
                                               mode="lines",
                                               name="Média")

    return number_of_papers_by_year_graph