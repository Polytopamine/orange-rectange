classdef Model
    %UNTITLED3 Summary of this class goes here
    %   Detailed explanation goes here

    properties
        min_sf
        node_list
        elem_list
        K  % stiffness matrix
        D  % displacement matrix
        F  % forces matrix
        unwn_force_locs
        F_m  % modified forces matrix, without the unknowns
        K_m  % modified stiffness matrix, without the unknowns
        D_m
    end

    methods
        function obj = Model(node_list,elem_list)
            % Construct an instance of this class
            %  Initializes the class
            obj.node_list = node_list;
            obj.elem_list = elem_list;

            %  find the smallest sf
            sf_list = [];
            for i = elem_list
                sf_list = cat(1,sf_list, i.sf);
            end
            obj.min_sf = min(sf_list);  % smallest sf of the list


            % turn the stiffnesses of the elements into multiples of the
            %  smallest sf
            for i = elem_list
                i.k = i.k * (i.sf / obj.min_sf);
            end

            % create an empty stiffness matrix for the elements
            %  using the node list
            obj.K = zeros(length(obj.node_list),length(obj.node_list));
            disp(obj.K)

            % add the sf of each elements using the node ids as the
            %  coordinates in the matrix
            for elem = obj.elem_list
                disp(elem)
                for i = 1:length(elem.nodes)
                    node_i = elem.nodes(i);
                    for j = 1:length(elem.nodes)
                        node_j = elem.nodes(j);
                        obj.K(node_i.ID, node_j.ID) = obj.K(node_i.ID, node_j.ID) + elem.k(i,j);
                    end
                end
            end
            disp(obj.K)



            % create stiffness matrix using the physical properties of the
            %  element materials
            obj.K = obj.K*obj.min_sf;
            disp(obj.K)



            % create displacement matrix
            obj.D = zeros(length(obj.node_list),1);
            disp(obj.D)
            for node_i = obj.node_list
                obj.D(node_i.ID) = node_i.displacement;
            end
            disp(obj.D)

            % create forces matrix
            obj.F = zeros(length(obj.node_list),1);
            disp(obj.F)
            for node_i = obj.node_list
                obj.F(node_i.ID) = node_i.force;
            end
            disp(obj.F)

            % solve the matrixes to calculate displacement
            % remove lines where the forces are unknown
            obj.unwn_force_locs = [];
            for i = 1:length(obj.F)
                F_i = obj.F(i);
                if isnan(F_i)  % NaN is used to denote an unknown value
                    obj.unwn_force_locs = [obj.unwn_force_locs, i];
                end
            end
            disp(obj.unwn_force_locs)

            %             disp([isnan(obj.F)]) % vector of NaN

            % remove lines and columns with unknown forces
            %             disp(obj.F(obj.unwn_force_locs))
            obj.F_m = obj.F;
            obj.F_m(obj.unwn_force_locs) = [];
            disp('F_m:')
            disp(obj.F_m)

            obj.K_m = obj.K(~isnan(obj.F), ~isnan(obj.F));
            %             disp('K:')
            %             disp(obj.K)
            disp('K_m:')
            disp(obj.K_m)

            % Solve equation to calculate displacements
            obj.D_m = obj.K_m'*obj.F_m;
            disp(obj.D_m)



            % calculate froces from displacement




            % update displacement values on the nodes
            % calculate stress and strain in teh elements based off node displacement








        end

        function outputArg = method1(obj,inputArg)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            outputArg = obj.min_sf + inputArg;
        end
    end
end