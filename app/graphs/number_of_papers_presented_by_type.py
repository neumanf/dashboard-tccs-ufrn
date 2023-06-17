import pandas as pd
import plotly.express as px

def get_number_of_papers_presented_by_type(df: pd.DataFrame):
    paper_type_counts = df['tipo_trabalho'].value_counts()

    num_papers_by_course_df = pd.DataFrame({
        "Tipo de trabalho": paper_type_counts.index,
        "Número de trabalhos": paper_type_counts.values,
    })

    top_5_courses_with_most_work_graph = px.bar(num_papers_by_course_df, x="Tipo de trabalho", y="Número de trabalhos")

    return top_5_courses_with_most_work_graph