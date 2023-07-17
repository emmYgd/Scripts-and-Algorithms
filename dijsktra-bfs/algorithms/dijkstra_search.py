# This is a sample Python script.
from typing import *
from heapq import heappop, heappush


# this is used for searching between weighted graphs nodes and neighbor in a network:
def dijkstra_search(weighted_graph: Dict, start_node: Sequence) -> Dict:
    # init:
    weights: Dict = {node: float('inf') for node in weighted_graph}
    weights[start_node] = 0
    priority_queue: List[Tuple] = [(0, start_node)]

    # loop through the priority queue:
    while priority_queue:
        # map heap priority queue into (weight, node) tuple:
        (current_weight, current_node) = heappop(priority_queue)

        if current_weight > weights[current_node]:
            continue

        for (neighbor, weight) in weighted_graph[current_node].items():
            distance = current_weight + weight
            if distance < weights[neighbor]:
                weights[neighbor] = distance
                heappush(priority_queue, (distance, neighbor))
    return weights

