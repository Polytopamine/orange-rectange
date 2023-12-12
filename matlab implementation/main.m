% F = 12;
% E = 10;
% L = 5000;
% A = 1000;
% 
% 
% n1 = Node(1, F, NaN);
% n2 = Node(2, F, NaN);
% n3 = Node(3, NaN, 10);
% 
% node_list = [n1 n2 n3];
% 
% 
% e1 = Element(1,[n1 n2],A,E,L);
% e2 = Element(2, [n2 n3], A, E, L);
% 
% 
% elem_list = [e1 e2];
% 
% Model1 = Model(node_list, elem_list);








%Tutuorial quesiton 1.10
E = 200000;
A = 1000000;
L = 1000;
F = 100;
%         ID, F, D
N0 = Node(1, NaN, 0);
N1 = Node(2, 3*F, NaN);
N2 = Node(3, 2*F, NaN);
N3 = Node(4, 1*F, NaN);
node_list = [N0 N1 N2 N3];
%            ID , nodes(list) , A , E , L
E0 = Element(1 , [N0 N1], 0.9*A , E , L );
E1 = Element(2 , [N1 N2], 0.6*A , E , L );
E2 = Element(3 , [N2 N3], 0.3*A , E , L );
elem_list = [E0 E1 E2];

Model(node_list, elem_list);


