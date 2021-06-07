'''
agents.py module contains the following classes which represent the methods used
{Greedy, Astar, BFS, DFS, UCS}
in addition to the class {Node} that represents each state
'''

from brains.agent_utils import sortH

class Node(object):
    def __init__(self, parent, data, cost, heuristic=0):
        self.parent = parent
        self.data = data
        self.cost = cost
        self.h = heuristic
        self.fn = cost + heuristic
        self.children = []

    def __lt__(self, other):
        return self.fn < other.fn

    def add_child(self, obj):
        self.children.append(obj)


class Greedy():
    def __init__(self, agentserver):
        self.server = agentserver
        self.start_state = agentserver.start_state
        self.root = Node(None, self.start_state, 0,
                         self.server.get_node_value(self.start_state))
        self.curNode = self.root
        self.fringe = [self.curNode]
        self.visited = []
        self.path = []

    def search(self):
        while not self.server.isGoal(self.curNode.data) and len(self.fringe) > 0:
            self.fringe.sort(key=sortH)
            self.curNode = self.fringe.pop(0)
            self.visited.append(self.curNode.data)
            self.expand()
            cost = 0

        if self.server.isGoal(self.curNode.data):
            node = self.curNode
            r_path = []
            while node != None:
                print(r_path)
                r_path.append(node.data)
                cost += node.cost
                node = node.parent
            print(r_path)
            r_path.reverse()
            self.path = r_path
            print("finally", r_path)
        return self.path, cost

    def expand(self):
        for i, n in enumerate(self.server.get_neighbours(self.curNode.data)):
            if n > 0 and (i not in self.visited):
                node = Node(self.curNode, i, n, self.server.get_node_value(i))
                self.curNode.add_child(node)
                self.fringe.append(node)

    def pprint_tree(self, node, file=None, _prefix="", _last=True):
        print(_prefix,  "|- ", node.data, sep="", file=file)
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, file, _prefix, _last)

    def display_Tree(self):
        self.pprint_tree(self.root)


class Astar():
    def __init__(self, agentserver):
        self.server = agentserver
        self.start_state = agentserver.start_state
        self.path = []
        self.fringe = []              # Stores whole nodes
        self.visited = []              # Stores node values only

    def search(self):

        # add first node

        self.fringe.append(Node(None, self.start_state,
                                     0, self.server.get_node_value(self.start_state)))

        while self.fringe:

            currNode = self.fringe[0]
            cost = 0
            self.fringe.pop(0)

            # Check if current node is the goal state: if yes, append and return path

            if self.server.isGoal(currNode.data):
                cost = currNode.cost
                self.path.append(currNode.data)
                if currNode not in self.visited:
                    self.visited.append(currNode.data)
                while currNode.parent != None:
                    currNode = currNode.parent
                    self.path.append(currNode.data)
                self.path.reverse()
                return self.path, cost

            # Expand node

            if currNode.data in self.visited:
                pass
            else:

                # add expanded nodes to fringe and order the fringe

                self.expand(currNode)
                self.fringe.sort()
                self.visited.append(currNode.data)

        return None, None

    def expand(self, currNode):
        for i, n in enumerate(self.server.get_neighbours(currNode.data)):
            if n > 0:
                node = Node(currNode, i, currNode.cost +
                                 n, self.server.get_node_value(i))
               # self.currNode.add_child(node)
                self.fringe.append(node)


class BFS():
    def __init__(self, agentserver):
        self.server = agentserver
        self.start_state = agentserver.start_state
        self.path = []
        self.fringe = []              # Stores whole nodes
        self.visited = []              # Stores node values only
        self.curr_node = None

    def search(self):
        self.fringe.append(Node(None, self.start_state,
                                0, self.server.get_node_value(self.start_state)))
        while len(self.fringe) !=0:
            curr_node = self.fringe.pop(0)
            self.curr_node = curr_node

            if curr_node.data not in self.visited:
                self.expand(curr_node)
                self.visited.append(curr_node.data)
            
            if self.server.isGoal(curr_node.data):
                return self.backPropagate(curr_node)

        return None, None

    def expand(self,curNode):
        self.curr_node = curNode
        for i, n in enumerate(self.server.get_neighbours(self.curr_node.data)):
            if n > 0 and (i not in self.visited):
                node = Node(self.curr_node, i, n,
                            self.server.get_node_value(i))
                self.curr_node.add_child(node)
                self.fringe.append(node)

    def backPropagate(self,currNode):
        cost = currNode.cost
        self.path.append(currNode.data)
        if currNode.data not in self.visited:
            self.visited.append(currNode.data)
        while currNode.parent != None:
            currNode = currNode.parent
            cost+=currNode.cost
            self.path.append(currNode.data)
        self.path.reverse()
        return self.path, cost


class DFS():
    def __init__(self, agentserver):
        self.server = agentserver
        self.start_state = agentserver.start_state
        self.path = []
        self.fringe = []              # Stores whole nodes
        self.visited = []              # Stores node values only
        self.curr_node = None

    def search(self):
        self.fringe.append(Node(None, self.start_state,
                                0, self.server.get_node_value(self.start_state)))
        while len(self.fringe) != 0:
            curr_node = self.fringe.pop()
            self.curr_node = curr_node

            if curr_node.data not in self.visited:
                self.expand(curr_node)
                self.visited.append(curr_node.data)

            if self.server.isGoal(curr_node.data):
                return self.backPropagate(curr_node)

        return None, None

    def expand(self, curNode):
        self.curr_node = curNode
        for i, n in enumerate(self.server.get_neighbours(self.curr_node.data)):
            if n > 0 and (i not in self.visited):
                print(i, self.visited)
                node = Node(self.curr_node, i, n,
                            self.server.get_node_value(i))
                self.curr_node.add_child(node)
                self.fringe.append(node)

    def backPropagate(self, currNode):
        cost = currNode.cost
        self.path.append(currNode.data)
        if currNode.data not in self.visited:
            self.visited.append(currNode.data)
        while currNode.parent != None:
            currNode = currNode.parent
            cost += currNode.cost
            self.path.append(currNode.data)
        self.path.reverse()
        return self.path, cost


class UCS():
    def __init__(self, agentserver):
        self.server = agentserver
        self.start_state = agentserver.start_state
        self.path = []
        self.fringe = []              # Stores whole nodes
        self.closed = []              # Stores node values only
        self.visited = []
        self.Node = Node

    def search(self):

        # add first node

        self.fringe.append(self.Node(None, self.start_state,
                                     0))

        while self.fringe:

            currNode = self.fringe[0]
            if currNode.data not in self.visited:
                self.visited.append(currNode.data)
            cost = 0
            self.fringe.pop(0)

            # Check if current node is the goal state: if yes, append and return path

            if self.server.isGoal(currNode.data):
                cost = currNode.cost
                self.path.append(currNode.data)
                while currNode.parent != None:
                    currNode = currNode.parent
                    self.path.append(currNode.data)
                self.path.reverse()
                return self.path, cost

            # Expand node

            if currNode.data in self.closed:
                pass
            else:
                # add expanded nodes to fringe and order the fringe

                self.expand(currNode)
                self.fringe.sort()
                self.closed.append(currNode.data)

        return None, None

    def expand(self, currNode):
        for i, n in enumerate(self.server.get_neighbours(currNode.data)):
            if n > 0:
                node = self.Node(currNode, i, currNode.cost +
                                 n)
               # self.currNode.add_child(node)
                self.fringe.append(node)
    