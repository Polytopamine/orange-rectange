'''
attempt to do the FEM optional coursework
goal is to make a 1D FEM solver that uses quadratic elemtents and can any number of displacement nodes
'''



import numpy as np
from operator import attrgetter
# from models import node_list , elem_list


def calculat_FEM(node_list, elem_list):
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


