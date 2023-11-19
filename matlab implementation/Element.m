classdef Element
    %UNTITLED5 Summary of this class goes here
    %   Detailed explanation goes here

    properties
        ID {mustBeNumeric}
        nodes
        A {mustBeNumeric} %Area
        E {mustBeNumeric} %mod of Elasicity
        L {mustBeNumeric} % Length
        sf {mustBeNumeric} % Stiffnes Fasctor
        k 
    end

    methods
        function obj = Element(ID, nodes, A, E, L)
            %UNTITLED5 Construct an instance of this class
            %   Detailed explanation goes here
            obj.ID = ID;
            obj.nodes = nodes;
            obj.A = A;
            obj.E = E;
            obj.L = L;
            
            obj.sf = (E*A)/L;

            if length(nodes) == 2 % the element is linear
                obj.k = [1 -1;-1 1]; 
            elseif length(nodes) == 3 % the element is quadratic
                obj.k = [7/3 -8/3, 1/3;-8/3 16/3 -8/3;1/3 -8/3 7/3];
            else
                disp('/!\ unsupported number of nodes per element')
            end
            
        end
    end

end