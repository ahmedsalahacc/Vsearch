'''
agent_utils.py module contains a class {AgentServer} that serves the Agents
and a function sortH() that is needed to sort the values in the list by heuristics
'''
import numpy as np
from math import fabs

class AgentServer():
    def __init__(self, adjMatrix, positions,start_state, goalNode, heuristics=None):
        # Adj Matrix is a normal 2d list n x n
        self.adjMatrix = np.array(adjMatrix)
        # Positions is a normal 2d list of size n*2 (x,y)
        self.positions = np.array(positions)
        # Goal nodes is the array that contains all nodes
        self.goalNodes = goalNode
        self.start_state = start_state
        self.manhattan = False
        if -1 not in heuristics:
            self.heuristics = np.array(heuristics)
        else:
            self.manhattan = True

    def get_neighbours(self, curState):
        # curState must be an integer indicating the state number
        return self.adjMatrix[curState]       
        
    def get_node_value(self, curState):
        # curState must be an integer indicating the state number
        if not self.manhattan:
            return self.heuristics[curState]
        p1 = self.positions[curState]
        h = []
        for g in self.goalNodes:
            x = self.positions[g][0]
            y = self.positions[g][1]
            h.append((fabs(p1[0]-x)+fabs(p1[1]-y))/1000)
        return min(h)

    def isConsistent(self):
        for f, t in enumerate(self.adjMatrix):
            for i, a in enumerate(t):
                if(a != 0):
                    if (self.get_node_value(f) - self.get_node_value(i)) > a:
                        return False
        return True

    def isGoal(self, curState):
        return curState in self.goalNodes

def sortH(a):
    return a.h