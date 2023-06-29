import networkx as nx
import matplotlib.pyplot as plt

# Leitura da tabela do arquivo
with open('tabela.txt', 'r') as file:
    lines = file.readlines()

# Remoção de caracteres de formatação e conversão para números
table = []
for line in lines:
    row = line.strip().split('\t')
    row = [0 if val == '-' else int(val) for val in row]
    table.append(row)

# Criação do grafo
G = nx.Graph()

# Adição dos vértices
num_vertices = len(table)
G.add_nodes_from(range(1, num_vertices + 1))

# Adição das arestas do grafo original
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        weight = table[i][j]
        if weight != 0:
            G.add_edge(i + 1, j + 1, weight=weight)

# Plotagem do grafo original
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo')

# Salvar a imagem do grafo
plt.savefig('grafo_original.png')

# Exibir a imagem do grafo
plt.show()