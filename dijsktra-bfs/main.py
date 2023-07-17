# This is a sample Python script.
from typing import *
from algorithms.dijkstra_search import dijkstra_search
from algorithms.breadth_first_search import breadth_first_search

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''weighted_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_node = 'A'
    shortest_weights: Dict = dijkstra_search(weighted_graph, start_node)
    print("Shortest weights from node 'A':", shortest_weights)'''

    graph = {
        'Emmy': ['James', 'Fisayo', 'Gates'],
        'Shawn': ['Penny', 'Dorcas', 'Victor'],
        'James': ['Drake', 'Grace', 'JoyS'],
        'Dorcas': ['Teni', 'Peace', 'Ebube']
    }

    start_node = 'Emmy'
    breadth_first_search(graph, start_node)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
