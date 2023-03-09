'''
attempt to do the FEM optional coursework
goal is to make a 1D FEM solver that uses quadratic elemtents and can any number of displacement nodes
'''



import numpy as np
import matplotlib.pyplot as plt
from operator import attrgetter



def calculate_FEM(node_list, elem_list):

    #find smallest stiffnessfactor of the elememts
    min_sf = min(elem_list , key=attrgetter('sf')).sf

    #make the stiffness be a multiple of the smallest stiffness value
    for i in elem_list:
        i.k = i.k * ( i.sf / min_sf )
        
    #create base stiffness matrix from elements
    K = np.zeros((len(node_list),len(node_list)))

    #add the stifness matrixs of each of the elements
    for elem in elem_list:
        for i in range(len(elem.nodes)):
            for j in range(len(elem.nodes)):

                K[elem.nodes[i].ID, elem.nodes[j].ID ] += elem.k[i,j]

    print(f'K :\n{K}')

    #create stiffness matrix that takes into account the properties of the elements by multiplying with the stifnessfactor
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





    # solving for displacement, first removing lines where the force is unknown because that would be unsolvable

    #determine the locations of unknown forces
    unwn_force_locs = []
    for i in range(len(F)):
        if np.isnan(F[i]) == True:
            unwn_force_locs.append(i)

    #remove lines and columns with unknown forces
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
    print('\nDisplacement at nodes:')
    for i in node_list:
        print(f'Node {i.ID} = {round(i.displacement[0],13):e} mm')

    print('\nForces at nodes :')
    for i in node_list:
        print(f'Node {i.ID} = {round(i.force[0],13):e} mm') #round the value to the 14th digit 
        #then turns into scientific notation to elimintae python rounding errors

    #calculate the stress and strain in each elemenent based on the displacement at the nodes
    print('\nStress and strain in each element :')
    for i in elem_list:

        i.strain = np.dot(np.array([-1/i.L , 1/i.L]),
                        np.array([i.nodes[0].displacement[0], i.nodes[len(i.nodes)-1].displacement[0]]))
        print(f'\nElem {i.ID} Strain = {i.strain:e}')

        i.stress = i.E * i.strain
        print(f'Elem {i.ID} Stress = {i.stress:e} MPa')

        




def find_displacement(elem, x, silent=0):
    #use the shape function to calculate the displacement at any point along the element
    
    if len(elem.nodes)==2: #linear element
        shape_function = np.array([1-x/elem.L, x/elem.L])
        displacement_array = np.array([elem.nodes[0].displacement,elem.nodes[1].displacement])

    if len(elem.nodes)==3: #quadratic element
        shape_function = np.array([1-3*x/elem.L + 2*x**2/elem.L**2 , 4*x/elem.L-4*x**2/elem.L**2 , -x/elem.L+2*x**2/elem.L**2])
        displacement_array = np.array([elem.nodes[0].displacement,elem.nodes[1].displacement,elem.nodes[2].displacement])
    
    # print(f'shape_function:\n{shape_function}')
    # print(f'displacement_array:\n{displacement_array}')
    
    displacement_x = np.dot(shape_function, displacement_array )

    if silent==0: #suppresses the print need be
        print(f'displacement at {x}mm into element{elem.ID}: {round(displacement_x[0],14)} mm')

    return displacement_x



def find_elem_displacement(elem):
    #finds the dispacement at mm along the element

    points = []
    disps = []

    for x in range(elem.L):

        points.append(x)
        disps.append(find_displacement(elem, x, 1)) #use 1 to keep the funtion silent

    return (points, disps)



def find_model_displacement(elem_list):

    points = []
    disps = []

    length_so_far = 0

    for i in range(len(elem_list)):
        # print(i)
        
        elem_points = find_elem_displacement(elem_list[i])[0]
        elem_disps = find_elem_displacement(elem_list[i])[1]


        elem_points = [p+length_so_far for p in elem_points] #increase the length by value of the previous elements
        # print(f'length added: {length_so_far}')

        length_so_far += elem_list[i].L
        points += elem_points
        disps += elem_disps

        # print(len(points))
        # print(points)

    return (points, disps)




def graph(points, disps):
    print('\ngraphing')
    print(f'number of points:{len(points)}\nnumber of displacement data: {len(disps)}')
    plt.plot(points, disps)
    plt.xlabel('distance (mm)')
    plt.ylabel('displacement (mm)')
    print('displaying graph')
    plt.show()
    print('graph done')






#still problems: 
# -- if both displacement and force is known, the force sill be overwritten by the calculation from the displacement
# -- the element stress and strain are not yet checked to work properly for quadratic (works good for linear) -- seems to be equal tho??
# -- would be cool to get the displacement along the length of the quad elements
# -- can only use point loads
# -- behavior whith assigned displacement seems odd- the rest ofthe displacement still increase regardless of which nodes should be fixed

