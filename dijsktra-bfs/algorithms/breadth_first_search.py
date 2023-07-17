# This is a sample Python script.
from typing import *
from collections import deque
from queue import Queue


# this is used for searching between non-weighted graphs nodes and neighbor in a network:
def breadth_first_search(graph: Dict, start_node: Sequence) -> Dict:
    # init

    # option 1: use Python's Queue from queue
    search_queue: Queue = Queue()
    # option 2: use Python's Deque from collection:
    # search_queue: Deque = deque()
    searched_neighbors: List = []

    # step through the graph:
    for each_node in graph:
        network_neighbors: List = graph[start_node]
        # start queueing neighbours:
        # for Queue:
        search_queue.put(network_neighbors)
        # for Deque:
        # search_queue.append(network_neighbors)
        '''start searching the search queue:
            # alternatively, u can use: for each_neighbor in search_queue:'''
        while search_queue:  # iterate search queue...
            # pop each person off Queue:
            each_direct_neighbor_nodes: List = search_queue.get()
            # pop each person off Dequeue:
            # each_person: str = search_queue.popleft()

            for each_person in each_direct_neighbor_nodes:
                if each_person in searched_neighbors:
                    # skip this loop round...
                    continue
                else:  # else isn't compulsory
                    is_person_seller: bool = person_is_seller(each_person)
                    if not is_person_seller:
                        # add each person's network to the queue:
                        # search_queue += graph[each_person]

                        if not graph[each_person]:
                            # skip this loop round if the neighbor doesn't have it's own neighbor:
                            continue
                        search_queue.put(graph[each_person])
                    else:
                        # print(each_person + "" + "is a seller")
                        # return True
                        return {'found_seller': each_person}


def person_is_seller(name: str) -> bool:
    # algorithm to check if someone is a seller - just a simple example:
    if name[-1] == 'S':
        return True
