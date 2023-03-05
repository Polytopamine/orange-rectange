'''
attempt to do the FEM optional coursework
goal is to make a 1D FEM solver that uses quadratic elemtents and can any number of displacement nodes
'''

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



import numpy as np
from operator import attrgetter
#from FEM_classes_definitions import Node , Element , node_list , elem_list


#-----------------------------------------------------------
'''
E = 200000
A = 100000
L = 5000
F = 100

#        ID , force, displacement --> None if unknown
N0 = Node(0 , None, 0)
N1 = Node(1 , 0, None)
N2 = Node(2 , F,    None)
N3 = Node(3 , None, 1)
N4 = Node(4 , 2*F,  5)

#           ID , nodes(list) , A , E , L
E0 = Element(0 , [N0 , N1 , N2], A , E , L )
E1 = Element(1 , [N2 , N3 , N4], 2*A , E , L )
'''



# 5.3--worked example 10
E = 200000
A = 1000000
L = 1000
F = 100
#        ID, F, D
N0 = Node(0, None, 0)
N1 = Node(1, 250, None)
N2 = Node(2, 100, None)
#           ID , nodes(list) , A , E , L
E0 = Element(0 , [N0, N1, N2], 0.1*A , E , 5*L )
#resuts as expected

'''
#Tutuorial quesiton 1.10
E = 200000
A = 1000000
L = 1000
F = 100
#         ID, F, D
N0 = Node(0, None, 0)
N1 = Node(1, 3*F)
N2 = Node(2, 2*F)
N3 = Node(3, 1*F)
#            ID , nodes(list) , A , E , L
E0 = Element(0 , [N0, N1], 0.9*A , E , L )
E1 = Element(1 , [N1, N2], 0.6*A , E , L )
E2 = Element(2 , [N2, N3], 0.3*A , E , L )
#results correct
'''
'''
#tutorial quesiton 2.3
E = 200000
A = 1000000
L = 10000

#         ID, F, D
N0 = Node(0, None, 0)
N1 = Node(1, 350)
N2 = Node(2, 100)

#            ID , nodes(list) , A , E , L
E0 = Element(0 , [N0, N1, N2], 0.4*A , E , L )
#results correct
'''




#-----------------------------------------------------------


#find smallest stiffnessfactor of the elememts
min_sf = min(elem_list , key=attrgetter('sf')).sf

#make the stiffness be a multiple of the smallest stiffness value
for i in elem_list:
    i.k = i.k * ( i.sf / min_sf )
    
#create base stiffness matrix from elements
#create the global K matrix using the multiples of the smallest value
K = np.zeros((len(node_list),len(node_list)))

for elem in elem_list:
    for i in range(len(elem.nodes)):
        for j in range(len(elem.nodes)):

            K[elem.nodes[i].ID, elem.nodes[j].ID ] += elem.k[i,j]

print(f'K :\n{K}')

#create stiffness matrix that takes into account the properties of the elements
K = K*min_sf
print(f"\nK*EA/L :\n{K}")

#create the displacement matrix
D = np.zeros((len(node_list),1))
for i in node_list:
    D[i.ID,0] = i.displacement
print(f'\nD :\n{D}')

#create the forces matrix
F = np.zeros((len(node_list),1))
for i in node_list:
    F[i.ID,0] = i.force
print(f'\nF :\n{F}')




# #solve for the displacements first

#remove lines and columns with unknown forces, 
# by deleting them instead of constructing anoother without them
# this is solving for displacement, so removing lines where the force is unknown because that would be unsolvable

#determine the locations of unknown forces
unwn_force_locs = []
for i in range(len(F)):
    if np.isnan(F[i]) == True:
        unwn_force_locs.append(i)


F_m = np.delete(F, unwn_force_locs, 0)
K_m = np.delete(np.delete(K, unwn_force_locs, 1), unwn_force_locs, 0)

# do matric operation to find the displacements
D_m = np.linalg.solve(K_m, F_m)


# with the displacements found, find the forces by usign another matrix operation
#Place the newfound displacements into the displacement matrix
# displacement was calculated from all known forces, so diplacement at unknown forces have not been found yet
new_disp_locs = np.delete(np.arange(len(F)), unwn_force_locs,0) 
for i in range(len(new_disp_locs)):
    D[new_disp_locs[i]] = D_m[i]
print(f'\nnew D:\n{D}')



#calculate the forces from the displacements
F = np.dot(K, D)
print(f'\nnew F:\n{F}')

#updates the displacement and force values on the nodes
for i in node_list:
    i.displacement = D[i.ID]
    i.force = F[i.ID]



#Display the force and dissplacement at each node
print('\nDissplacement at nodes:')
for i in node_list:
    print(f'Node {i.ID} = {round(i.displacement[0],14):e} mm')

print('\nForces at nodes :')
for i in node_list:
    print(f'Node {i.ID} = {round(i.force[0],14):e} mm') #round the value to the 14th digit 
    #then turns into scientific notation to elimintae python rounding errors

#calculate the stress and strain in each elemenent based on the displacement at the nodes
print('\nStress and strain in each element :')
for i in elem_list:

    i.strain = np.dot(np.array([-1/i.L , 1/i.L]),
                      np.array([i.nodes[0].displacement[0], i.nodes[len(i.nodes)-1].displacement[0]]))
    print(f'\nElem {i.ID} : Strain = {i.strain:e}')

    i.stress = i.E * i.strain
    print(f'Elem {i.ID} : Stress = {i.stress:e} MPa')

    



#still problem: 
# -- if both displacement and force is known, 
# the force sill be overwritten by the calculation from the displacement
# -- the element stress and strain are not yet checked to work properly for quadratic (works good for linear)
# -- would be cool to get the displacement along the length of the quad elements


