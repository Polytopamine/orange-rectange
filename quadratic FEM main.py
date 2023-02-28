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

#        ID , force, displacement) null if unknown
N0 = Node(0 , None, 0)
N1 = Node(1 , 0, None)
N2 = Node(2 , F, None)
# N3 = Node(3 , 0, 0)
# N4 = Node(4 , 2*F, None)


#           ID , nodes(list) , A , E , L
E0 = QuadraticElement(0 , [N0 , N1 , N2], 2*A , E , L )
# E1 = QuadraticElement(0 , [N2 , N3 , N4], 2*A , E , L )
'''
E1 = LinearElement(1 , N1 , N2 , 2*A , 2*E , L )
E2 = LinearElement(2 , N2 , N3 , A , 2*E , L )
E3 = LinearElement(3 , N3 , N4 , 2*A , E , L )
E4 = LinearElement(4 , N4 , N5 , A , 2*E , 2*L )
E5 = LinearElement(5 , N5 , N6 , 2*A , 2*E , 2*L )
'''








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




#determine the number of unknwon displacements
nb_unwn_disp = 0
for i in D:
    if np.isnan(i) == True:
        nb_unwn_disp += 1

#determine the number of unknwon forces
nb_unwn_force = 0
for i in F:
    if np.isnan(i) == True:
        nb_unwn_force += 1
print(nb_unwn_disp, nb_unwn_force)


#solve for the displacements first
#remove lines that have unknown forces
D_m = np.zeros((len(D)-nb_unwn_force,1))
F_m = np.zeros((len(D)-nb_unwn_force,1))
K_m = np.zeros((len(D)-nb_unwn_force,len(D)))

counter = 0 # used because teh modified metricies are smaller than the original
for i in range(len(F)):
    # print(i)
    # print(D[i])
    # print(np.isnan(D[i]))
    # print(K[i])
    if np.isnan(F[i]) == False: 
        

        D_m[counter] = D[i]
        F_m[counter] = F[i]
        K_m[counter] = K[i]
        counter += 1
        print(D_m)
        print(F_m)
        print(K_m)

        pass


