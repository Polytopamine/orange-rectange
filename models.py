

from FEM_classes_definitions import Node , Element , node_list , elem_list
import FEM_math






'''
#worked example 7 from lecture 4:
E = 200000  #=200*10^3N/mm2
A = 1000000 #=1m2
L = 1000 #mm
F = 100 #N
N0 = Node(0, None, 0)
N1 = Node(1, 0)
N2 = Node(2, 100)
E0 = Element(0, [N0, N1, N2], 0.1*A , E , 5*L )
FEM_math.calculate_FEM(node_list, elem_list)

# #-- work example above, but using a 2 noded element:
# N0 = Node(0, None, 0)
# N1 = Node(1, 100)
# E0 = Element(0, [N0, N1], 0.1*A , E , 5*L )
# FEM_math.calculate_FEM([N0,N1], [E0])
#gets the same results


FEM_math.find_displacement(E0, 10)
a=FEM_math.find_elem_displacement(E0)
FEM_math.graph(a[0],a[1])
'''

'''
#lecture 3 example 4
E = 200000  #=200*10^3N/mm2
A = 1000000 #=1m2
L = 1000 #mm = 1m
F = 100 #N
N0 = Node(0, None, 0)
N1 = Node(1, 100)
E0 = Element(0, [N0, N1], 0.1*A , E , 4*L )
FEM_math.calculate_FEM([N0,N1], [E0])
#gets the same results

FEM_math.find_displacement(E0, 3500)
FEM_math.find_elem_displacement(E0)
'''



#other models from the different worked examples:


E = 200000
A = 100000
L = 5000
F = 100

#        ID , force, displacement --> None if unknown
N0 = Node(0 , None, 0)
N1 = Node(1 , 0, None)
N2 = Node(2 , F,    None)
N3 = Node(3 , None, 0)
N4 = Node(4 , 2*F)

#           ID , nodes(list) , A , E , L
E0 = Element(0 , [N0 , N1 , N2], A , E , L )
E1 = Element(1 , [N2 , N3 , N4], 2*A , E , L )

FEM_math.calculate_FEM([N0,N1,N2,N3,N4], [E0,E1])

a=FEM_math.find_elem_displacement(E1)
FEM_math.graph(a[0],a[1])


'''
# 5.3--worked example 10
E = 200000  #=200*10^3N/mm2
A = 1000000 #=1m2
L = 1000 #mm
F = 100 #N
#        ID, F, D
N0 = Node(0, None, 0)
N1 = Node(1, 250, None)
N2 = Node(2, 100, None)
#           ID , nodes(list) , A , E , L
E0 = Element(0 , [N0, N1, N2], 0.1*A , E , 5*L )
#resuts as expected
'''





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




