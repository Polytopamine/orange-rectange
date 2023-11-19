F = 12;
E = 10;
L = 5000;
A = 1000;


n1 = Node(1, F, 78);
n2 = Node(2, 2*F, 655);
n3 = Node(3, NaN, 13);

node_list = [n1 n2 n3];


e1 = Element(1,[n1 n2],A,E,L);
e2 = Element(2, [n2 n3], A, E, 0.5*L);


elem_list = [e1 e2];
Model(node_list, elem_list);


