import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():

    """
    Stack = last-in first-out
    """
    
    def __init__(self):
        self.frontier = []

    """
    A function that initially creates a frontier
    that will be initially represented using an empty list
    """

    def add(self, node):
        self.frontier.append(node)

    """
    Adds a node to the empty frontier
    """

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    """
    A function that checks if the frontier contains a node
    """

    def empty(self):
        return len(self.frontier) == 0
    
    """
    Checks if the frontier is empty.
    Which means the length of the frontier list is 0
    """

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node