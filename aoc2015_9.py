import networkx as nx


f = open('aoc09.txt','r')
input_text = f.readlines()
f.close()
G = nx.Graph()
city_names = set()
for line in input_text:
    my_line = line.strip()
    distance = int(my_line.split(' = ')[1])
    cities = my_line.split(' = ')[0].split(' to ')
    G.add_edge(cities[0], cities[1], weight=distance)
    city_names.add(cities[0])
    city_names.add(cities[1])

city_names = list(city_names)
#optimal_path = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
#optimal_path_length = dict(nx.all_pairs_dijkstra_path_length(G))
possible_paths = []
shortest_path = 10000000000000000000000
longest_path = 0
for source in list(G.nodes):
    for dest in list(G.nodes):
        if source == dest:
            continue
        pair_paths = list(nx.shortest_simple_paths(G, source, dest, 'weight'))
        for path in pair_paths:
            if len(path) < len(list(G.nodes)):
                continue
            current_distance = 0
            for edge in xrange(0,len(path)-1):
                current_distance += G[path[edge]][path[edge+1]]['weight']
            if current_distance < shortest_path:
                shortest_path = current_distance
            if current_distance > longest_path:
                longest_path = current_distance
print('Part 1: shortest distance is ' + str(shortest_path))
print('Part 2: longest distance is ' + str(longest_path))