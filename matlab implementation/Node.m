
classdef Node
    %Node is the class that stores the data for each node that can be used
    %for defining elements
    %   Detailed explanation goes here

    properties
        ID {mustBeNumeric}  % used to place the stifness factor, cannot be less than 1
        force {mustBeNumeric}
        displacement {mustBeNumeric}
    end


    methods
        function obj = Node(ID, force, displacement)
            %UNTITLED2 Construct an instance of this class
            %   Detailed explanation goes here
            obj.ID = ID;
            obj.force = force;
            obj.displacement = displacement;

        end
    end
end



