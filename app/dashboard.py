import dash
import pandas as pd

from dash import dcc
from dash import html

from app.graphs.course_with_most_papers_in_the_last_5_years import get_course_with_most_papers_in_the_last_5_years
from app.graphs.top_5_courses_with_most_work import get_top_5_courses_with_most_work
from app.utils import sanitize_dataframe

app = dash.Dash(__name__, external_stylesheets=['../assets/css/index.css'])
server = app.server

# Import data and drop rows with missing values, if any
df = pd.read_csv('../data/tccs.csv', sep=';')

# Process and sanitize dataframe
df = sanitize_dataframe(df)

# Get top 5 courses in regard to works production
top_5_courses_with_most_work_graph = get_top_5_courses_with_most_work(df)

# Course with most papers produced in the last 5 years
course_with_most_papers_graph, course_with_most_papers = get_course_with_most_papers_in_the_last_5_years(df)

app.layout = html.Div(children=[
    html.H1(children='Trabalhos de Conclusão de Curso (UFRN)'),

    html.Div(children='''
        Top 5 cursos que mais entregam trabalho
    '''),

    dcc.Graph(
        id='top-5-courses-graph',
        figure=top_5_courses_with_most_work_graph
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