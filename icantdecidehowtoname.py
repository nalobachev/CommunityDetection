import networkx as nx
import csv
import matplotlib.pyplot as plt
from random import choice
import community

with open('data.csv', 'r') as csvfile:
    people = csv.reader(csvfile, delimiter=',')
    groups = {}
    for row in people:
        number = row[0]
        groups[number] = set(row[1:])

G = nx.Graph()
sorted(groups)
# for key in groups:
#     G.add_node(key)
for key in groups:
    for key2 in groups:
        common = len(groups[key] & groups[key2])
        if (common > 15) and (key != key2) and (key2 > key):
            G.add_edge(key, key2, capacity=common)
        else:
            continue
# nx.draw_circular(G, node_color='#FF8C30')
nx.draw(G, with_labels=False, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=15)
plt.show()


def splitting(graph):
    copy = graph.copy()
    while True:
        source = choice(list(copy.nodes()))
        sink = choice(list(copy.nodes()))
        while source == sink:
            sink = choice(list(copy.nodes()))
        cut_value, partition = nx.minimum_cut(copy, source, sink)
        reachable, non_reachable = partition
        if min(len(reachable), len(non_reachable)) > 5:
            break
    if len(reachable) < len(non_reachable):
        for node in reachable:
            for neighbour in copy.neighbors(node):
                if neighbour not in reachable:
                    graph.remove_edge(node, neighbour)
    else:
        for node in non_reachable:
            for neighbour in copy.neighbors(node):
                if neighbour not in non_reachable:
                    graph.remove_edge(node, neighbour)
    if nx.number_connected_components(graph) < 3:
        splitting(graph)


splitting(G)
nx.draw(G, with_labels=False, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=15)
plt.show()

partition = community.best_partition(H)
best = nx.Graph()
best.add_edges_from([pair for pair in partition.items() if pair[1] == 1])
nx.draw(best, with_labels=True, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=5)
plt.show()
