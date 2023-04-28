
% eigenvalues

%sigma_ij = [5,0,0;0,-6,-12;0,-12,1]
sigma_ij = [32,11,0;11,8,0;0,0,7]

eignevalues = eig(sigma_ij)

max_shear = (eignevalues(3) - eignevalues(1))/2
max_normal = (eignevalues(3) + eignevalues(1))/2


[V, D] = eig(sigma_ij)