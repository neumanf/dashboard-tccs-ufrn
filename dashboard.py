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

df = pd.DataFrame({
    "Curso": num_papers_by_course.index,
    "Número de trabalhos": num_papers_by_course.values,
})

top_5_courses = px.bar(df, x="Curso", y="Número de trabalhos")

app.layout = html.Div(children=[
    html.H1(children='Trabalhos de Conclusão de Curso (UFRN)'),

    html.Div(children='''
        Top 5 cursos que mais entregam trabalho
    '''),

    dcc.Graph(
        id='top-5-courses-graph',
        figure=top_5_courses
    )
])

if __name__ == '__main__':
    app.run_server(port=5000, debug=True, use_reloader=False)