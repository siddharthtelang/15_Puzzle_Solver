#!/usr/bin/python3

# ========================================
# ENPM661 Spring 2021: Planning for Autonomous Robots
# Given a initial states of a 15 puzzle, reach the goal state
# Keep a track of parent nodes to back trace from goal to initial state
#
# Author: Siddharth Telang(stelang@umd.edu)
# ========================================
# Run as 'python3 15_puzzle_solver.py --case test5'
# To run other test cases, replace the argument of --case with the test case number

import argparse
import array
import copy
import numpy as np

# define a Queue class for storing the nodes to be expanded
class Queue:

    # init function
    def __init__(self):
        self.queue = []

    # insert in queue
    def enque(self, item):
        self.queue.insert(0, item)

    # pop node
    def deque(self):
        if self.queue:
            return self.queue.pop()
        return 'Empty'

    # check if queue is not empty
    def not_empty(self):
        return (len(self.queue) > 0)

    # check if the queue contains a specific list item
    def contains(self, item):
        return (item in self.queue)

    # print the queue
    def __print__(self):
        print(self.queue)

# define a class Node for storing all nodes generated in puzzle with parent node info
class Node:

    # init function to store info about:
    # child: array, its respective list/state, and generated by which move - left/right/up/down
    # parent: index, array and list/state form
    def __init__(self, arr, parent_index, parent_state):
        self.arr = arr # child array - store parent array for now ; it will be modified with movements of blank tile
        self.list = [] # child list
        self.parent_index = parent_index # parent index
        self.parent_arr = arr # parent array
        self.parent_state = parent_state # parent list/state form
        self.move = ''

