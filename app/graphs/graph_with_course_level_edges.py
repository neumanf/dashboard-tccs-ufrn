import networkx as nx
import plotly.graph_objects as go


def create_graph_with_course_level_edges(dataframe):
    dataframe = dataframe.head(20)

    # Criar um grafo direcionado (DiGraph) usando a NetworkX
    graph = nx.DiGraph()

    # Adicionar nós ao grafo usando o título do trabalho como identificador único
    for index, row in dataframe.iterrows():
        graph.add_node(row['titulo'])

    # Adicionar arestas ao grafo usando curso e nível como atributos
    for index, row in dataframe.iterrows():
        for index2, row2 in dataframe.iterrows():
            if row['curso'] == row2['curso'] and row['nivel'] == row2['nivel'] and index != index2:
                graph.add_edge(row['titulo'], row2['titulo'], curso=row['curso'], nivel=row['nivel'])

    # Layout do grafo para visualização
    pos = nx.spring_layout(graph)

    # Criar o objeto de figura usando Plotly
    fig = go.Figure()

    # Adicionar os nós ao gráfico
    for node in graph.nodes:
        x, y = pos[node]
        fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text', marker=dict(size=10), text=node, textposition="top center"))

    # Adicionar as arestas ao gráfico
    for edge in graph.edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        fig.add_trace(go.Scatter(x=[x0, x1, None], y=[y0, y1, None], mode='lines', line=dict(width=0.5), hoverinfo='none'))

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Grafo de Trabalhos de Conclusão de Curso (20 primeiros dados)',
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    return fig