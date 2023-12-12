from FEM_classes_definitions import Node , Element , node_list , elem_list
import FEM_functions


# file in which the problem is defined and the fuctions are run to solve the problem

# --to create a model:

# -create nodes with:
#     Nx = Node(ID, Force, Displacement)
#     where:
#         Nx is the name of the node object, for use in defining the elements and in lists of nodes
#         ID is the number of the node, used for its loction in matrixes and naming it in the output
#         Force is the force applied to the node in N. Use None to indicate it is unknown
#         Displacement is the amount of displacement at the node in mm. Use None indicates it is unkown.
#             If force and displacement are assumed to be 0 and unkown respectively if ommited

# -Create elements with:
#     Ex = Element(ID , List of nodes , Area , E , Length )
#     where:
#         Ex is the name of the element object, for use in ists of nodes
#         ID is the number of the element, used for its loction in matrixes and naming it in the output
#         List of nodes must contain a list of the nodes to which the element is contected, e.g.: [Nx , Ny , Nz]
#             Can contain 2 or 3 nodes to make a linear of quadratic element respectively
#         Area is the area of the element in mm2
#         E is the young's modulus of the element in N/mm2
#         Lenght is the length of the element in mm

        
        
# --Solve the FEM model
        
# -Compute the forces and displacements at the nodes with:
#    FEM_math.calculate_FEM(node_list, elem_list)
#     where:
#         node_list is a list of the nodes in the model, eg [Nw, Nx , Ny , Nz]
#         elem_list is a list of the elements in the model eg [Ex, Ey]
#             node_list and elem_list are lists all nodes and elements respectively and can be used if only one model is being used at a time

#     Function solves for the the displacement and forces at the nodes and modifies the values in the node object to reflect the new values
#     prints all the steps taken and the different matrixes at different stages

    


# --To find displacement isplacements:

# -Find displacement at x in an element:        
#     find_displacement(element, x, silent=0)
#     where:
#         element is the element object
#         x is the lenght in mm
#         silent == 1 supresses the print of the result

#     returns the displacement at x in mm


# -Find displacement at points throughout the elements:
#     find_elem_displacement(element)
#         where:
#             element is the name of the element object
    
#     retrns a tuple of list of the displacement at every milimeter of the element: ([Xs], [displacements])

# -Find the displacements at every mm of the model
#     find_model_displacement(element_list)
#     where:
#         element_list is a list of the elements to be evaluated 

#     retrns a tuple of list of the displacement at every milimeter of the elements: ([Xs], [displacements])

    
# -Graph the results
#     graph(points, displacement)
#     where :
#         points is a list milimeters
#         displacement is a list of the displacements at the every milimeter

#     plots a graph for x-disp
    
#     Returns None
            












#random collection of exercises and test models:






# # Using both linear and quadratic elements
# E = 200000  # =200*10^3N/mm2
# A = 100000 # =1m2
# L = 5000  # mm
# F = 100  # N

# #        ID , force, displacement --> None if unknown
# N0 = Node(0 , F, None)
# N1 = Node(1 , None, 0)
# N2 = Node(2 , 2*F, None)
# N3 = Node(3 , -0.5*F, None)
# N4 = Node(4 , 0, None)

# #           ID , nodes(list) , A , E , L
# E0 = Element(0 , [N0 , N1], A , E , L )
# E1 = Element(1 , [N1 , N2], A , E , L )
# E2 = Element(2 , [N2 , N3, N4], A , E , 2*L )
# # E3 = Element(3 , [N3 , N4], A , E , L )

# # node_list = [N0,N1,N2,N3,N4]
# # elem_list = [E0,E1,E2,E3]

# FEM_functions.calculate_FEM(node_list, elem_list)
# a=FEM_functions.find_model_displacement(elem_list)
# # FEM_functions.simple_graph(a)






# #worked example 7 from lecture 4:
# E = 200000  #=200*10^3N/mm2
# A = 1000000 #=1m2
# L = 1000 #mm
# F = 100 #N
# N0 = Node(0, None, 0)
# N1 = Node(1)
# N2 = Node(2, 100)
# E0 = Element(0, [N0, N1, N2], 0.1*A , E , 5*L )
# FEM_math.calculate_FEM(node_list, elem_list)

# # #-- work example above, but using a 2 noded element:
# # N0 = Node(0, None, 0)
# # N1 = Node(1, 100)
# # E0 = Element(0, [N0, N1], 0.1*A , E , 5*L )
# # FEM_math.calculate_FEM([N0,N1], [E0])
# #gets the same results


# FEM_math.find_displacement(E0, 10)
# a=FEM_math.find_elem_displacement(E0)
# FEM_math.graph(a[0],a[1])




# #lecture 3 example 4
# E = 200000  #=200*10^3N/mm2
# A = 1000000 #=1m2
# L = 1000 #mm = 1m
# F = 100 #N
# N0 = Node(0, None, 0)
# N1 = Node(1, 100)
# E0 = Element(0, [N0, N1], 0.1*A , E , 4*L )
# FEM_math.calculate_FEM([N0,N1], [E0])
# #gets the same results

# FEM_math.find_displacement(E0, 3500)
# FEM_math.find_elem_displacement(E0)





# E = 200000
# A = 100000
# L = 5000
# F = 100

# #        ID , force, displacement --> None if unknown
# N0 = Node(0 )
# N1 = Node(1 , None, 0)
# N2 = Node(2 , 2*F,    None)
# N3 = Node(3 , None, 0)
# N4 = Node(4 )

# #           ID , nodes(list) , A , E , L
# E0 = Element(0 , [N0 , N1 , N2], A , E , L )
# E1 = Element(1 , [N2 , N3 , N4], 2*A , E , L )

# FEM_functions.calculate_FEM([N0,N1,N2,N3,N4], [E0,E1])

# a=FEM_functions.find_elem_displacement(E1)
# # FEM_functions.simple_graph(a)
# a=FEM_functions.find_model_displacement([E0,E1])
# FEM_functions.simple_graph(a)







# # 5.3--worked example 10
# E = 200000  #=200*10^3N/mm2
# A = 1000000 #=1m2
# L = 1000 #mm
# F = 100 #N
# #        ID, F, D
# N0 = Node(0, None, 0)
# N1 = Node(1, 250, None)
# N2 = Node(2, 100, None)
# #           ID , nodes(list) , A , E , L
# E0 = Element(0 , [N0, N1, N2], 0.1*A , E , 5*L )
# FEM_functions.calculate_FEM(node_list, elem_list)
# #resuts as expected







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
FEM_functions.calculate_FEM(node_list, elem_list)
#results correct




# #tutorial quesiton 2.3
# E = 200000
# A = 1000000
# L = 10000
# #         ID, F, D
# N0 = Node(0, None, 0)
# N1 = Node(1, 350)
# N2 = Node(2, 100)
# #            ID , nodes(list) , A , E , L
# E0 = Element(0 , [N0, N1, N2], 0.4*A , E , L )
# FEM_functions.calculate_FEM(node_list, elem_list)
# #results correct

