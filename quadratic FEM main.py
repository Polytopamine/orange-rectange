'''
attempt to do the FEM optional coursework
goal is to make a 1D FEM solver that uses quadratic elemtents and can any number of displacement nodes
'''



#define the system
#stifness matrix
#displacement metrix





#FEM classes definitions

import numpy as np




elem_list = []
node_list = []

class QuadraticElement:
    """gives the attributes of the element"""
    def __init__(self , ID , nodes , A , E , L):
        self.ID = ID
        self.nodes = nodes # should be a list of the different elements

        self.A = A 
        self.E = E 
        self.L = L 
        self.sf = (E*A)/L 
        self.k = np.array([[7/3, -8/3, 1/3],[-8/3, 16/3, -8/3],[1/3, -8/3, 7/3]])

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

E = 210000
A = 100
L = 15000
F = 100

#        ID , force, displacement --> None if unknown
N0 = Node(0 , None, 0)
N1 = Node(1 , 0, None)
N2 = Node(2 , F, None)
N3 = Node(3 , None, 1)
N4 = Node(4 , 2*F, None)


#           ID , nodes(list) , A , E , L
E0 = QuadraticElement(0 , [N0 , N1 , N2], 2*A , E , L )
E1 = QuadraticElement(0 , [N2 , N3 , N4], 2*A , E , L )


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


    #create the global K matrix using the multiples


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


#create the forces matrix

F = np.zeros((len(node_list),1))

for i in node_list:
    F[i.ID,0] = i.force

print('\nF :')
print(F)


#create the displacement matrix

D = np.zeros((len(node_list),1))

for i in node_list:
    D[i.ID,0] = i.displacement

print('\nD :')
print(D)



 
#determine the locations of unknown displacements

unwn_disp_locs = []
for i in range(len(D)):
    if np.isnan(D[i]) == True:
        unwn_disp_locs.append(i)
# print(unwn_disp_locs)

#determine the locations of unknown forces
unwn_force_locs = []
for i in range(len(F)):
    if np.isnan(F[i]) == True:
        unwn_force_locs.append(i)
# print(unwn_force_locs)






# #solve for the displacements first

#try to remove lines and columns with unknown forces, 
# by deleting them instead of constructing anoother without them
# solving for displacement, so roving lines where the force is unknown because that would be unsolvable

F_m = np.delete(F, unwn_force_locs, 0)
print('F_m')
print(F_m)
K_m = np.delete(np.delete(K, unwn_force_locs, 1), unwn_force_locs, 0)
print('K_m')
print(K_m)




# do matric operation to find the displacements


D_m = np.linalg.solve(K_m, F_m)
print('D_m:')
print(D_m)


# with the displacements found, find the forces by usign another matrix operation

#Place the newfound displacements into the displacement matrix

new_disp_locs = np.delete(np.arange(len(F)), unwn_force_locs,0) # displacement was calculated from all known forces, so diplacement at unknown forces have not been found yet
# print(np.arange(len(F)),unwn_force_locs, new_disp_locs )
for i in range(len(new_disp_locs)):
    # print(i)
    # print(D_m[i])
    D[new_disp_locs[i]] = D_m[i]

print('new D:')
print(D)


#find the remaining unknown forces from the displacements







####testing stuff:

# print('\nK:')
# print(K)
# # A = K * [[True],[True],[False]]
# # A = K [True,True,False]
# # print(A)
# # print(A[0,0])
# print('\n')
# A = np.delete(K,1,0)
# print(A)
# print('\n')
# A = np.delete(K,[0,1],0)
# print(A)

# A = np.arange(25).reshape(5,5)
# print(A)
# print('\n')
# A = np.delete(A,[1,1,1,1,1],0)
# print(A)

# a = [1,0,0,1,0]
# b=[]
# for i in range(len(a)): 
#     if a[i] ==1 :
#         b.append(i)
# print(b)
