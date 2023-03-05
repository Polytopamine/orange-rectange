
#FEM classes definitions

import numpy as np

elem_list = []
node_list = []

k_quadratic = np.array([[7/3, -8/3, 1/3],[-8/3, 16/3, -8/3],[1/3, -8/3, 7/3]])
k_linear = np.array([[1,-1],[-1,1]])

class Element:
    """gives the attributes of the element"""
    def __init__(self , ID , nodes , A , E , L):
        self.ID = ID
        self.nodes = nodes # should be a list of the different nodes the element is conmected to

        self.A = A 
        self.E = E 
        self.L = L 
        self.sf = (E*A)/L 

        if len(nodes) == 2 : self.k = k_linear
        if len(nodes) == 3 : self.k = k_quadratic

        elem_list.append(self)



class Node:
    """ details info on the node"""
    def __init__(self, ID , force=0, displacement=None):
        self.ID = ID
        self.force = force
        self.displacement = displacement

        node_list.append(self)  




