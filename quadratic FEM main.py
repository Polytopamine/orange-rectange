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


# E1 = LinearElement(1 , N1 , N2 , 2*A , 2*E , L )
# E2 = LinearElement(2 , N2 , N3 , A , 2*E , L )
# E3 = LinearElement(3 , N3 , N4 , 2*A , E , L )
# E4 = LinearElement(4 , N4 , N5 , A , 2*E , 2*L )
# E5 = LinearElement(5 , N5 , N6 , 2*A , 2*E , 2*L )




#-----------------------------------------------------------

#find smallest stiffnessfactor of the elememts

min_sf = min(elem_list , key=attrgetter('sf')).sf

#find what the others are the multiple of the smallest
for i in elem_list:
    i.k = i.k * ( i.sf / min_sf )

    #create the global K matrix using the multiples of the smallest value


#create base stiffness matrix from elements

K = np.zeros((len(node_list),len(node_list)))

for elem in elem_list:
    for i in range(len(elem.nodes)):
        for j in range(len(elem.nodes)):

            K[elem.nodes[i].ID, elem.nodes[j].ID ] += elem.k[i,j]


print('K :')
print(K)


#create stiffness matrix that takes into account the properties of the elements
K = K*min_sf
print("\nK*EA/L :")
print(K)

#create the displacement matrix
D = np.zeros((len(node_list),1))
for i in node_list:
    D[i.ID,0] = i.displacement
print('\nD :')
print(D)


#create the forces matrix
F = np.zeros((len(node_list),1))
for i in node_list:
    F[i.ID,0] = i.force
print('\nF :')
print(F)





# #solve for the displacements first

#try to remove lines and columns with unknown forces, 
# by deleting them instead of constructing anoother without them
# solving for displacement, so removing lines where the force is unknown because that would be unsolvable

#determine the locations of unknown forces
unwn_force_locs = []
for i in range(len(F)):
    if np.isnan(F[i]) == True:
        unwn_force_locs.append(i)
# print(unwn_force_locs)


F_m = np.delete(F, unwn_force_locs, 0)
# print('F_m')
# print(F_m)
K_m = np.delete(np.delete(K, unwn_force_locs, 1), unwn_force_locs, 0)
# print('K_m')
# print(K_m)


# do matric operation to find the displacements
D_m = np.linalg.solve(K_m, F_m)
# print('D_m:')
# print(D_m)


# with the displacements found, find the forces by usign another matrix operation

#Place the newfound displacements into the displacement matrix

new_disp_locs = np.delete(np.arange(len(F)), unwn_force_locs,0) # displacement was calculated from all known forces, so diplacement at unknown forces have not been found yet
# print(np.arange(len(F)),unwn_force_locs, new_disp_locs )
for i in range(len(new_disp_locs)):
    D[new_disp_locs[i]] = D_m[i]

print('\nnew D:')
print(D)
#new D seems correct accroding to worked example 7 lecture 4






#find the remaining unknown forces from the displacements

#determine the locations of unknown displacements
unwn_disp_locs = []
for i in range(len(D)):
    if np.isnan(D[i]) == True:
        unwn_disp_locs.append(i)
# print(unwn_disp_locs)

#create new d and f matrixes without the unknow displacement locations
D_m = np.delete(D, unwn_disp_locs, 0)
# print('D_m')
# print(D_m)
K_m = np.delete(np.delete(K, unwn_disp_locs, 1), unwn_disp_locs, 0)
# print('K_m')
# print(K_m)

#calculate the forces from the displacements
F = np.dot(K_m, D_m)
print('\nnew F:')
print(F)
#seems correct, thought the rounding on the 0 is very slightly off

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
    # print(f'Elem {i.ID} :')

    i.strain = np.dot(np.array([-1/i.L , 1/i.L]),np.array([i.nodes[0].displacement[0], i.nodes[len(i.nodes)-1].displacement[0]]))
    # print(np.array([-1/i.L , 1/i.L]))
    # print(np.array([i.nodes[0].displacement[0], i.nodes[len(i.nodes)-1].displacement[0]]))
    # print(np.dot(np.array([-1/i.L , 1/i.L]),np.array([i.nodes[0].displacement[0], i.nodes[2].displacement[0]])))
    print(f'\nElem {i.ID} : Strain = {i.strain:e}')

    i.stress = i.E * i.strain
    print(f'Elem {i.ID} : Stress = {i.stress:e} MPa')

    