
% findign the normal and shear composnents of stress on a plane from the
% stress at a point

%stress_at_point = [2,1,3; 1,2,-2; 3,-2,1]
%stress_at_point = [2,1,0;1,3,-2;0,-2,1]
stress_at_point = [32,11,0;11,8,0;0,0,7]
%disp(stress_at_point)

%nomral_of_plane = 1/3*[1;2;-2]
%nomral_of_plane = 1/sqrt(2)*[1;0;1]
nomral_of_plane = 1/3*[sqrt(7),1,1].'
%disp(nomral_of_plane)




stress_of_plane = (stress_at_point * nomral_of_plane)
%disp(stress_of_plane)

normal_stress = stress_of_plane' * nomral_of_plane
shear_stress = sqrt(norm(stress_of_plane)^2-normal_stress^2)

a = 1/sqrt(2)
rotation_about =  [a,0,-a; 0,1,0;a,0,a]

rotated_stress = rotation_about * stress_at_point * rotation_about'




