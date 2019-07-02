import networkx as nx
import csv
import matplotlib.pyplot as plt
from random import choice
import time
import community


def splitting(graph):
    copy = graph.copy()
    while True:
        source = choice(list(copy.nodes()))
        sink = choice(list(copy.nodes()))
        while source == sink:
            sink = choice(list(copy.nodes()))
        cut_value, partition = nx.minimum_cut(copy, source, sink)
        reachable, non_reachable = partition
        if min(len(reachable), len(non_reachable)) > 7:
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


def draw_friends(graph):
    components = nx.connected_components(graph)
    fgraph = nx.Graph()
    for component in components:
        print(len(component))
        # friends_number = 0
        for element in component:
            if element in friends.keys():
                for friend in (component & friends[element]):
                    fgraph.add_edge(element, friend)
    print('friends')
    for component in nx.connected_components(fgraph):
        print(len(component))
    nx.draw(fgraph, with_labels=True, node_color='green', node_size=50, edge_color='black', linewidths=1, font_size=5)
    plt.show()


def splitting_count_time():
    start_time = time.time()
    splitting(G)
    print("--- %s seconds ---" % (time.time() - start_time))


with open('data.csv', 'r') as csvfile:
    people = csv.reader(csvfile, delimiter=',')
    groups = {}
    for row in people:
        number = row[0]
        groups[number] = set(row[1:])


with open('data3.csv', 'r') as csvfile2:
    people = csv.reader(csvfile2, delimiter=',')
    friends = {}
    for row in people:
        number = row[0]
        friends[number] = set(row[1:])


G = nx.Graph()
sorted(groups)
sorted(friends)

for key in groups:
    for key2 in groups:
        common = len(groups[key] & groups[key2])
        if (common > 15) and (key != key2) and (key2 > key):
            G.add_edge(key, key2, capacity=common)
        else:
            continue

nx.draw(G, with_labels=False, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=15)
plt.show()

splitting(G)
nx.draw(G, with_labels=True, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=5)
plt.show()


partition = community.best_partition(H)
best = nx.Graph()
best.add_edges_from([pair for pair in partition.items() if pair[1]==1])
nx.draw(best, with_labels=True, node_color='orange', node_size=50, edge_color='black', linewidths=1, font_size=5)
plt.show()


draw_friends(G)
splitting_count_time()
