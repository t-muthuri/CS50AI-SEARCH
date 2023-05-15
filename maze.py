import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():

    """
    Stack = last-in first-out
    This class implements the idea of a frontier
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
        
    """
    check if the frontier is empty and raise an exception error
    else remove the last-in node and create a new list
    then expand on the node removed
    """

    class QueueFrontier(StackFrontier):

        """
        Inherits functions from the StackFrontier
        except from how it removes the nodes
        Queue = first-in first-out
        """

        def remove(self):
            if self.empty():
                raise Exception("empty frontier")
            else:
                node = self.frontier[0]
                self.frontier = self.frontier[1:]
                return node
            
class Maze():
    def __init__(self, filename):
        
        #Read file and set height and width of the maze
        with open(filename) as f:
            contents = f.read()