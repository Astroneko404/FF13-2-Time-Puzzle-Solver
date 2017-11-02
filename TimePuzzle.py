#!/usr/bin/env python
"""
This file helps solve the Time Puzzle in Final Fantasy xiii-2.

Users will type each number appearing in the order of clockwise,
seperated by apace character(" "), and it will calculate one solution
automatically

I made it just for fun :D
Some algorithms of Hamiltonian paths are from:
    http://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/

Updating:
Ver 1.0.1: Fixed an iteration bug
"""
__author__ = "Astronoid_404"
__date__ = "11/01/2017"
__version__ = "1.0.1"

class Node:
    def __init__(self, value):
        """
            Constructor of a node

            Args:
                value (int): the number value of a node

            Returns:
                none
            """
        self.next = []
        self.pos = 0
        self.value = value


class LabyrinthSolver:
    def __init__(self):
        """
            Constructor of a Graph for puzzle solving

            Args:
                none

            Returns:
                none
            """
        self.data = []
        self.size = 0

    def hm_helper(self, node, path, pos):
        """
            A recursive part to calculate the hamiltonian path

            Args:
                node (Node): The node which users start calculate from
                path (list): A integer list storing the node visited
                pos (int): A integer that record current position in path

            Returns:
                bool: 1 if successful, 0 if failed
            """
        if pos == self.size:
            # If all nodes are visited
            if sorted(path) == list(range(self.size)):
                return 1
            else:
                return 0
        for next_node in node.next:
            path[pos] = node.pos
            if self.hm_helper(next_node, path, pos+1) == 1:
                return 1
            else:
                path[pos] = -1
        return 0

    def import_list(self, node_list):
        """
            Import the node information from user-inputs

            Args:
                node_list (list): the list of number typed by users

            Returns:
                none
            """
        # Assign each node with a position idx
        for i in range(len(node_list)):
            new_node = Node(node_list[i])
            self.data.append(new_node)
            self.data[i].pos = i
        self.size = len(node_list)

    def make_graph(self):
        """
            Connect each node in self.data
            Nodes are connected according to their value:
            A node should connect with its two children, which has pos
            p'= p +- (value in the node). If not in range [0, n-1],
            the p' should be take (mod n)

            Args:
                none

            Returns:
                none
        """
        for node in self.data:
            v = node.value
            p = node.pos
            # Append the next node on the clockwise pos
            next1 = p + v
            if next1 >= self.size:
                next1 = next1 - self.size
            node.next.append(self.data[next1])
            # Append the next node on the counter-clockwise pos
            next2 = p - v
            if next2 < 0:
                next2 = next2 + self.size
            node.next.append(self.data[next2])
            #print '{}[{}], Left[{}], Right[{}]'.format(v, p, next1, next2)

    def print_result(self, path):
        """
            Print the path

            Args:
                path (list): the path being printed

            Returns:
                none
            """
        print 'Here is the result:'
        for idx in path:
            print '{}[{}]'.format(self.data[idx].value, self.data[idx].pos)

    def search_route(self):
        """
            The main function that searches a Hamitonian path of a graph.
            After calculating, it will print a path

            Args:
                none

            Returns:
                none

            """
        route_path = [-1] * self.size
        found = False
        for i in range(0, self.size - 1):
            if self.hm_helper(self.data[i], route_path, 0) == 1:
                found = True
                break
        if found:
            self.print_result(route_path)
        else:
            print 'There is no such path'


while True:
    print '================================================'
    v = raw_input('Please input each node in clockwise order: '
                  '(Seperate them by space)\n')
    test_list = [int(i) for i in v.split()]
    graph = LabyrinthSolver()
    graph.import_list(test_list)
    graph.make_graph()
    graph.search_route()
    while True:
        q = raw_input("Continue? (y/n)\n")
        if q == 'n':
            exit()
        elif q == 'y':
            break
        else:
            print 'Invalid input'
        print '\n'