'''
env_utils.py module serves the agent_utils.py module by providing handy
functions that percieve the environment
'''

import numpy as np

__all__ = ['process_graph']


def get_adj_matrix(connections, graph_type=0):
    '''
    input: connections list
    graph_type: 0 => directed and 1=> undirected 
    output: adjacency matrix represented by alphabitical order in rows and columns
    '''
    n = len(connections)
    adj_matrix = np.zeros((n, n))
    #loop over every node
    for i in range(n):
        # loop over its connections
        for j in range(len(connections[i]['children_nodes'])):
            # retrieve the displacement of the letter from the character 'A'
            displacement = ord(connections[i]['children_nodes'][j])-ord('A')
            # add its respective weight to its displacement index in the adjacency matrix
            adj_matrix[i][displacement] = connections[i]['weights'][j]

            # add undirected graph mirroring if the graph is undirected
            if graph_type:
                adj_matrix[displacement][i] = connections[i]['weights'][j]

    return adj_matrix


def extract_heuristics(connections):
    '''
    inputs: connections list
    output: list of heuristics represented alphabetically
    '''
    return [i['heuristics'] for i in connections]


def process_graph(dic):
    '''
    inputs: takes the dictionary of the parameters sent from the server
    output: dictionary with the processed keys which are
        [start,'goal','method','adj_matrix','heuristics']
    '''
    base_letter_encoding = ord('A')
    start, method = ord(dic["start"]) - base_letter_encoding, dic['method']
    goals = [(ord(i)-base_letter_encoding) for i in dic["goal"]]
    print(goals)
    connections = dic['connections']
    is_directed = int(dic['is_undirected']);
    adj_matrix = get_adj_matrix(connections,is_directed)
    heuristics = extract_heuristics(connections)
    positions = [node['pos'] for node in connections]

    return {
        'start': start,
        'goal': goals,
        'method': method,
        'adj_matrix': adj_matrix.tolist(),
        'heuristics': heuristics,
        'positions': positions
    }
