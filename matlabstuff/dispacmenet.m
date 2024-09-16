
%find the displacement field
disp(" -- find the displacement field --\n")


syms x1 x2 x3 a

% ux = x1*(1+x3^2);
% uy = x2*(1+x1^2);
% uz = x3*(1+x2^2);
% ux = (x1-x3)^2;
% uy = (x2+x3)^2;
% uz = -x1*x2;

ux = a^2*(x2^2*x1 + x2)+a*x1^2*x2;
uy = a^2 * x2*x3^2 + a*x2^2*x3;
uz = a^2 * x3^2*x1;

point = [4,2,2];
a_value = 1*10^-9;

e1 = [1,0,0]';
e2 = [0,1,0]';
n = 1/sqrt(3)*[1,1,1].'
Enn = 2.5*10^-8;
m = 1/sqrt(2)*[1,0,1].'
k = 1/sqrt(2)*[1,1,0].'



displacement_gradient = [diff(ux, x1), diff(ux, x2), diff(ux, x1); 
    diff(uy, x1), diff(uy, x2), diff(uy, x3); 
    diff(uz, x1), diff(uz, x2), diff(uz, x3)];

disp(" displacement_gradient:")
disp(displacement_gradient)

linear_strain_tensor = 0.5*(displacement_gradient + displacement_gradient.');

disp("linear strain tensor:")
disp(linear_strain_tensor)


linear_strain_at_P = subs(subs(subs(linear_strain_tensor, x1, point(1)), x2, point(2)), x3, point(3));
disp("linear strain at P:")
disp(linear_strain_at_P)

strain_towards_e1 = e1.'*linear_strain_tensor*e1

strain_towards_n_from_P = n.'*linear_strain_at_P*n
strain_towards_n_from_P_calc_1 = n.'*linear_strain_at_P

a_sol = solve(strain_towards_n_from_P == Enn, a );
disp(round(a_sol,5))






E_P_a = subs(linear_strain_at_P, a, a_value);
vpa(subs(E_P_a, a, a_value), 5)
disp("Emm:")
%vpa(m.'*E_P_a, 5)
vpa(m.'*E_P_a*m, 5)

disp("Ek:")
vpa(k.'*E_P_a, 5)
vpa(k.'*E_P_a*k, 5)


E_P_a = subs(linear_strain_at_P, a, a_sol(1));
vpa(subs(E_P_a, a, a_value), 5)
disp(round(a_sol(1),5))
vpa(subs(E_P_a, a, a_value), 5)
vpa(n.'*E_P_a*n, 5)



 