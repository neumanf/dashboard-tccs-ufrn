import pandas as pd
import plotly.express as px

def get_course_with_most_papers_in_the_last_5_years(df: pd.DataFrame):
    current_year = 2023
    last_five_years = df[df['ano'].str.split('.').str[0].astype(int) >= current_year - 5]
    course_with_most_papers = last_five_years['curso'].value_counts().index[0]
    course_last_five_years = last_five_years[last_five_years['curso'] == course_with_most_papers].groupby(['ano']).size().reset_index(name='works_count')

    course_with_most_papers_df = pd.DataFrame({
        "Ano": course_last_five_years.ano,
        "Número de trabalhos": course_last_five_years.works_count,
    })

    course_with_most_papers_graph = px.bar(course_with_most_papers_df, x="Ano", y="Número de trabalhos", color="Ano")
    
    return course_with_most_papers_graph, course_with_most_papers