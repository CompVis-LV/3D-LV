%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function returns a point1 oe point2 in lines which has not yet been 
% place in a polygon.
% lineIndex shows what line to pick, pt gives the end, point1 or point2
% Inputs lines (all lines) and polyg (already assigned lines)

function [lineIndex, pt] = unassignedPoint(lines, polyg)
    % Looks through all possible lines
    for countLines = 1:length(lines)
        diffent = 0;
        for countpolyg = 1:length(polyg)
            point1 = lines(countLines).point1;
            check1 = [polyg(countpolyg, 1), polyg(countpolyg, 2)];
            check2 = [polyg(countpolyg, 3), polyg(countpolyg, 4)];
            % Checks to see if point1 exists in a polygon already
            a = isequal(point1, check1);
            b = isequal(point1, check2);
            % Counting how many times point is not assigned 
            if a == 0 && b == 0
                diffent = diffent +1;
            end
        end
        % If point1 wasnt equal to any of the previous polygon points
        if diffent == length(polyg)
            lineIndex = countLines ;     % returns index to unassigned point
            pt = 1;
            return
        end
        % Checks for point2's if no point1's were unassigned
        diffent = 0;
        for countpolyg = 1:length(polyg)
            point2 = lines(countLines).point2;
            check1 = [polyg(countpolyg, 1), polyg(countpolyg, 2)];
            check2 = [polyg(countpolyg, 3), polyg(countpolyg, 4)];
            a = isequal(point2, check1);
            b = isequal(point2, check2);
            if a == 0 && b == 0;
                diffent = diffent +1;
            end
        end
        if diffent == length(polyg)
            lineIndex = countLines;     % returns index to unassigned point
            pt = 2;
            return
        end
    end
    % Returns zeros to show no unassigned points
    lineIndex = 0;
    pt = 0;
end