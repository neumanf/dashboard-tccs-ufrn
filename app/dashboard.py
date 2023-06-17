import os
import dash
import pandas as pd
import dash_mantine_components as dmc

from dash import dcc
from dash import html
from dash_iconify import DashIconify

from app.graphs.course_with_most_papers_in_the_last_5_years import get_course_with_most_papers_in_the_last_5_years
from app.graphs.number_of_papers_by_advisor import get_number_of_papers_by_advisor
from app.graphs.number_of_papers_presented_by_type import get_number_of_papers_presented_by_type
from app.graphs.top_5_courses_with_most_work import get_top_5_courses_with_most_work
from app.utils import sanitize_dataframe

app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ]
)
server = app.server

# Import data
df = pd.read_csv('../data/tccs.csv', sep=';')

# Process and sanitize dataframe
df = sanitize_dataframe(df)

row_count = len(df.index)
column_count = len(df.columns)
file_size = round(os.path.getsize("../data/tccs.csv") / 1024.0 / 1024.0, 2)
analysis_period = f"{df['ano'].min()} - {df['ano'].max()}"

top_5_courses_with_most_work_graph = get_top_5_courses_with_most_work(df)
course_with_most_papers_graph, course_with_most_papers = get_course_with_most_papers_in_the_last_5_years(df)
number_of_papers_by_advisor_graph = get_number_of_papers_by_advisor(df)
number_of_papers_presented_by_type_graph = get_number_of_papers_presented_by_type(df)

app.layout = dmc.MantineProvider(
    [
        html.Div(
            [
                dmc.Header(
                    [
                        dmc.Container(
                            [
                                dmc.Text("Trabalhos de Conclusão de Curso (UFRN)", fw="bold"),
                                dmc.Group(
                                    [
                                        dmc.Anchor(
                                            dmc.Tooltip(
                                                dmc.ActionIcon(
                                                    DashIconify(icon="icon-park-outline:source-code", width=20),
                                                    size="lg",
                                                ),
                                                label="Dataset",
                                            ),
                                            href="https://dados.ufrn.br/dataset/trabalhos-de-conclusao-de-curso",
                                        ),
                                        dmc.Anchor(
                                            dmc.Tooltip(
                                                dmc.ActionIcon(
                                                    DashIconify(icon="bi:github", width=20),
                                                    size="lg",
                                                ),
                                                label="Código fonte",
                                            ),
                                            href="https://github.com/neumanf/dashboard-tccs-ufrn",
                                        ),
                                    ]
                                )
                            ],
                            size="80%",
                            pt="md",
                            style={"display": "flex", "justifyContent": "space-between"}
                        )
                    ],
                    height=60,
                    withBorder=True,
                    mb="md"
                ),
                dmc.Container(
                    [
                        dmc.Title("Dashboard", order=3, mb="lg"),
                        dmc.Group(
                            [
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="icon-park-twotone:data-all", width=20),
                                                dmc.Title("Total de dados analisados", order=5),
                                            ],
                                            mb="sm"
                                        ),
                                        dmc.Text(row_count)
                                    ],
                                    style={"width": "22em"}
                                ),
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="carbon:data-2", width=20),
                                                dmc.Title("Total de características", order=5),
                                            ],
                                            mb="sm"
                                        ),
                                        dmc.Text(column_count)
                                    ],
                                    style={"width": "22em"}
                                ),
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="ph:file-csv", width=20),
                                                dmc.Title("Tamanho do arquivo", order=5),
                                            ],
                                            mb="sm"
                                        ),
                                        dmc.Text(f"{file_size} MiB")
                                    ],
                                    style={"width": "22em"}
                                ),
                                dmc.Card(
                                    [
                                        dmc.Group(
                                            [
                                                DashIconify(icon="tabler:clock-hour-4", width=20),
                                                dmc.Title("Período de análise", order=5),
                                            ],
                                            mb="sm"
                                        ),
                                        dmc.Text(analysis_period)
                                    ],
                                    style={"width": "22em"}
                                )
                            ],
                            mb="xl"
                        ),
                        dmc.Grid(
                            [
                                dmc.Col(
                                    dmc.Card(
                                        [
                                            dmc.Title("Top 5 cursos que mais entregam trabalho", order=5, mb="sm"),
                                            dmc.CardSection(
                                                dcc.Graph(
                                                    id='top-5-courses-graph',
                                                    figure=top_5_courses_with_most_work_graph
                                                )
                                            ),
                                        ],
                                        withBorder=True,
                                        shadow="sm",
                                        radius="md",
                                        style={"width": 700},
                                    ),
                                    span=6
                                ),
                                dmc.Col(
                                    dmc.Card(
                                        [
                                            dmc.Title(f"Distribuição de trabalhos do curso {course_with_most_papers} nos últimos 5 anos", order=5, mb="sm"),
                                            dmc.CardSection(
                                                dcc.Graph(
                                                    id='course-with-most-papers-produced-in-the-last-5-years-graph',
                                                    figure=course_with_most_papers_graph
                                                )
                                            ),
                                        ],
                                        withBorder=True,
                                        shadow="sm",
                                        radius="md",
                                        style={"width": 700},
                                    ),
                                    span=6
                                ),
                                dmc.Col(
                                    dmc.Card(
                                        [
                                            dmc.Title(
                                                "Top 10 número de trabalhos por orientador",
                                                order=5, mb="sm"),
                                            dmc.CardSection(
                                                dcc.Graph(
                                                    id='number-of-papers-by-advisor-graph',
                                                    figure=number_of_papers_by_advisor_graph
                                                )
                                            ),
                                        ],
                                        withBorder=True,
                                        shadow="sm",
                                        radius="md",
                                        style={"width": 700},
                                    ),
                                    span=6
                                ),
                                dmc.Col(
                                    dmc.Card(
                                        [
                                            dmc.Title(
                                                "Tipos de trabalho mais apresentados",
                                                order=5, mb="sm"),
                                            dmc.CardSection(
                                                dcc.Graph(
                                                    id='number-of-papers-presented-by-type-graph',
                                                    figure=number_of_papers_presented_by_type_graph
                                                )
                                            ),
                                        ],
                                        withBorder=True,
                                        shadow="sm",
                                        radius="md",
                                        style={"width": 700},
                                    ),
                                    span=6
                                )
                            ],
                            gutter="lg",
                            mb="lg"
                        ),
                    ],
                    size="80%",
                ),
            ],
            style={"height": "100vh"}
        )
    ],
    theme={
        "colorScheme": "dark",
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "components": {
            "Button": {"styles": {"root": {"fontWeight": 400}}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
            "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
        },
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True
)

if __name__ == '__main__':
    app.run_server(port=5000, debug=True, use_reloader=False)