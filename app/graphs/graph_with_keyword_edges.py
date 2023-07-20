import networkx as nx
import plotly.graph_objects as go


def create_graph_with_keyword_edges(dataframe):
    # Selecionar os 10 primeiros registros do DataFrame
    dataframe = dataframe.head(10)

    # Criar um grafo não direcionado (Graph) usando a NetworkX
    graph = nx.Graph()

    # Adicionar nós ao grafo usando o título do trabalho como identificador único
    for index, row in dataframe.iterrows():
        graph.add_node(row['titulo'])

    # Adicionar arestas ao grafo com base nas palavras-chave em comum
    for index, row in dataframe.iterrows():
        for index2, row2 in dataframe.iterrows():
            if index != index2:
                keywords1 = set(str(row['palavras_chave']).split('.'))
                keywords2 = set(str(row2['palavras_chave']).split('.'))
                common_keywords = keywords1.intersection(keywords2)
                if len(common_keywords) > 0:
                    graph.add_edge(row['titulo'], row2['titulo'], keywords=list(common_keywords))

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
        keywords = ', '.join(graph[edge[0]][edge[1]]['keywords'])
        fig.add_trace(go.Scatter(x=[x0, x1, None], y=[y0, y1, None], mode='lines', line=dict(width=0.5), hoverinfo='text', text=keywords))

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Grafo de Trabalhos de Conclusão de Curso (10 primeiros dados)',
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    return fig
