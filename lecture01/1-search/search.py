import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self, node):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        # return any(node.state == state for node in self.frontier)
        for node in self.frontier:
            if node.state == state:
                return True
        return False
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] #0 es el primer elemento, -1 es el último (da la vuelta)
            self.frontier = self.frontier[:-1]# elimina el último nodo de la frontera
            return node
        
    
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:] # elimina el primer nodo de la frontera
            return node