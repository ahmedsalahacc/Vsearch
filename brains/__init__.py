'''
brains module returns the function [serve] that serves the request to solve
the search problem
'''
from brains.env_utils import process_graph
from brains.agent_utils import *
from brains.agents import *

def serve(obj):
    # extract info and prepare server
    graph_dict = process_graph(obj)
    server = AgentServer(
        adjMatrix=graph_dict['adj_matrix'],
        positions=graph_dict['positions'],
        start_state=graph_dict['start'],
        goalNode=graph_dict['goal'],
        heuristics=graph_dict['heuristics']
    )

    # initializers
    method = graph_dict['method']  # which search algorithm
    searcher = None
    if method == 'Greedy':
        searcher = Greedy(server)
    elif method == 'A*':
        searcher = Astar(server)
    elif method == 'BFS':
        searcher = BFS(server)
    elif method == 'DFS':
        searcher = DFS(server)
    else:
        searcher = UCS(server)

    # search
    path, cost = searcher.search()
    visited = searcher.visited
    print('\n\n')
    print("Is MANHATTAN:",server.manhattan,'\n')
    return {
        'path': path,
        'cost': cost,
        'visited': visited,
        'method':method
    }