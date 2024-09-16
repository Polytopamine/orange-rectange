%Mohr Coulomb stress
 
t_0 = 70;
phi = pi/7;
sigma1 = 100;
sigma2=40;
sigma3=-20;


t_max = (sigma1-sigma3)/2
sigma_n = (sigma1+sigma3)/2
t = sigma_n * tan(phi)+t_0
SF = t/t_max