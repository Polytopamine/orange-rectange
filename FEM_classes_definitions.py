
#FEM classes definitions

import numpy as np

elem_list = []
node_list = []

k_quadratic = np.array([[7/3, -8/3, 1/3],[-8/3, 16/3, -8/3],[1/3, -8/3, 7/3]])
k_linear = np.array([[1,-1],[-1,1]])

class Element:
    """gives the attributes of the element"""
    def __init__(self , ID , nodes , A , E , L):

        '''
        ID is the number of the element, used for its loction in matrixes and naming it in the output  
        List of nodes must contain a list of the nodes to which the element is contected, e.g.: [Nx , Ny , Nz]   
            Can contain 2 or 3 nodes to make a linear of quadratic element respectively  
        Area is the area of the element in mm2  
        E is the young's modulus of the element in N/mm2  
        Lenght is the length of the element in mm  
        '''

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
    """ info on the node"""
    def __init__(self, ID , force=0, displacement=None):

        '''
        ID is the number of the node, used for its loction in matrixes and naming it in the output  
        Force is the force applied to the node in N. Use None to indicate it is unknown  
        Displacement is the amount of displacement at the node in mm. Use None indicates it is unkown.  
            If force and displacement are assumed to be 0 and unkown respectively if ommited  
        '''
        
        self.ID = ID
        self.force = force
        self.displacement = displacement

        node_list.append(self)  




