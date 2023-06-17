import pandas as pd
import plotly.express as px

def get_top_5_courses_with_most_work(df: pd.DataFrame):
    num_papers_by_course = df['curso'].value_counts().head(5)

    num_papers_by_course_df = pd.DataFrame({
        "Curso": num_papers_by_course.index,
        "Número de trabalhos": num_papers_by_course.values,
    })

    top_5_courses_with_most_work_graph = px.bar(num_papers_by_course_df, x="Curso", y="Número de trabalhos")

    return top_5_courses_with_most_work_graph