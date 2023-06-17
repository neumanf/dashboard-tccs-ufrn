import dash

from dash import dcc
from dash import html

import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Import data and drop rows with missing values, if any
df = pd.read_csv('tccs.csv', sep=';')
df.dropna(inplace=False)

# As it has many inconsistent dates, it was necessary to remove the column so as not to affect the analyses
df = df.drop('data_defesa', axis=1)

df['ano'] = df['ano'].astype(str)
df['ano'] = df['ano'].str.split('.').str[0]

# Get top 5 courses in regards to works production
num_papers_by_course = df['curso'].value_counts().head(5)

num_papers_by_course_df = pd.DataFrame({
    "Curso": num_papers_by_course.index,
    "Número de trabalhos": num_papers_by_course.values,
})

top_5_courses_graph = px.bar(num_papers_by_course_df, x="Curso", y="Número de trabalhos")

# Course with most papers produced in the last 5 years
current_year = 2023
last_five_years = df[df['ano'].str.split('.').str[0].astype(int) >= current_year - 5]
course_with_most_papers = last_five_years['curso'].value_counts().index[0]
course_last_five_years = last_five_years[last_five_years['curso'] == course_with_most_papers].groupby(['ano']).size().reset_index(name='works_count')

course_with_most_papers_df = pd.DataFrame({
    "Ano": course_last_five_years.ano,
    "Número de trabalhos": course_last_five_years.works_count,
})

course_with_most_papers_graph = px.bar(course_with_most_papers_df, x="Ano", y="Número de trabalhos", color="Ano")

app.layout = html.Div(children=[
    html.H1(children='Trabalhos de Conclusão de Curso (UFRN)'),

    html.Div(children='''
        Top 5 cursos que mais entregam trabalho
    '''),

    dcc.Graph(
        id='top-5-courses-graph',
        figure=top_5_courses_graph
    ),

    html.Div(children=f'''
        Distribuição de trabalhos do curso {course_with_most_papers} nos últimos 5 anos
    '''),

    dcc.Graph(
        id='course-with-most-papers-produced-in-the-last-5-years-graph',
        figure=course_with_most_papers_graph
    )
])

if __name__ == '__main__':
    app.run_server(port=5000, debug=True, use_reloader=False)