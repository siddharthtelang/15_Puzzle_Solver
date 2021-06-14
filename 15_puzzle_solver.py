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

    # store the index of the blank / zero block to find the moves
    def set_blank_index(self, i, j):
        self.i = i
        self.j = j

    # make list of character values from current child array
    def make_list(self):
        if (len(self.arr) > 0):
            a = self.arr.ravel()
            for i in a:
                self.list.append(i)

    # print the child list
    def print_list(self):
        print(self.list)

# function to find the moves from the parent node
def find_moves(i, j, parent):
    moves = ['up', 'down', 'left', 'right']
    boundary = parent.arr.shape[0]
    if (j == 0):
        moves.remove('left')
    if (j == boundary-1):
        moves.remove('right')
    if (i == 0):
        moves.remove('up')
    if (i == boundary-1):
        moves.remove('down')
    return moves

# function to move the blank element to left and return the array
def ActionMoveLeft(node):
    arr = node.arr
    i, j = node.i, node.j
    arr[i][j], arr[i][j-1]  = arr[i][j-1], arr[i][j]
    return arr

# function to move the blank element to right and return the array
def ActionMoveRight(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return arr

# function to move the blank element up and return the array
def ActionMoveUp(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
    return arr

# function to move the blank element down and return the array
def ActionMoveDown(node):
    i, j = node.i, node.j
    arr = node.arr
    arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
    return arr

# convert to string list
def convert2List(arr):
    a = (np.array(arr)).ravel()
    return [str(i) for i in a]

# define function to calculate path
def path(inital):

    toTest = convert2List(inital)

    # final goal state
    final = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']

    # convert final goal state and inital state to array
    final_arr = np.reshape(final, (4,4))
    toTest_arr = np.reshape(toTest, (4,4))

    # initialize queue which will store the nodes to be expanded. By default, store the test case state
    mainQueue = Queue()
    mainQueue.enque(toTest)

    # print the initial stage - list and array
    print('Initial Stage:')
    mainQueue.__print__()
    print(toTest_arr)
    print('\n')

    # define flag to set if goal reached and a count for number of expansions
    flag, count = 0, 0

    # define mainList which stores all the nodes expanded and append the test case
    mainList = []
    mainList.append(toTest)

    # define a list to back trace the goal state. This will hold all the object of nodes traversed
    backTrack = []

