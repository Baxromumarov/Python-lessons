# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



from display import Displayable

class Node(Displayable):
 """A node in a search tree. It has a
 name a string
 isMax is True if it is a maximizing node, otherwise it is minimizing
node
 children is the list of children
 value is what it evaluates to if it is a leaf.
 """
def __init__(self, name, isMax, value, children):
 self.name = name
 self.isMax = isMax
 self.value = value
 self.allchildren = children

def isLeaf(self):
 """returns true of this is a leaf node"""
 return self.allchildren is None



def children(self):
 """returns the list of all children."""
 return self.allchildren
def evaluate(self):
 """returns the evaluation for this node if it is a leaf"""
 return self.value



fig10_5 = Node("a",True,None, [
Node("b",False,None, [
Node("d",True,None, [
Node("h",False,None, [
Node("h1",True,7,None),
Node("h2",True,9,None)]),
Node("i",False,None, [
Node("i1",True,6,None),
Node("i2",True,888,None)])]),
Node("e",True,None, [
Node("j",False,None, [
Node("j1",True,11,None),
Node("j2",True,12,None)]),
Node("k",False,None, [
Node("k1",True,888,None),
Node("k2",True,888,None)])])]),
Node("c",False,None, [
Node("f",True,None, [
Node("l",False,None, [
Node("l1",True,5,None),
Node("l2",True,888,None)]),
Node("m",False,None, [
Node("m1",True,4,None),
Node("m2",True,888,None)])]),
Node("g",True,None, [
Node("n",False,None, [
Node("n1",True,888,None),
Node("n2",True,888,None)]),
Node("o",False,None, [
Node("o1",True,888,None),
Node("o2",True,888,None)])])])])






















