%% pointsUnclassified
%Returns a point1 in lines which has not yet been place in a polygon 

function [lineIndex, pt] = unassignedPoint(lines, poly)

%rows = any(isnan(poly),2);
%poly(rows,:) = []

%poly = poly(sum(isnan(poly),4)==0)

    for countLines = 1:length(lines)
        diff = 0;
        for countPoly = 1:length(poly)
            point1 = lines(countLines).point1;
            check1 = [poly(countPoly, 1), poly(countPoly, 2)];
            check2 = [poly(countPoly, 3), poly(countPoly, 4)];

            a = isequal(point1, check1);
            b = isequal(point1, check2);
        
            if a == 0 && b == 0
                diff = diff +1;
            end
        end
        if diff == length(poly)
            lineIndex = countLines ;     % returns index to unassigned point
            pt = 1;
            return
        end

        
        diff = 0;
        for countPoly = 1:length(poly)
            point2 = lines(countLines).point2;
            check1 = [poly(countPoly, 1), poly(countPoly, 2)];
            check2 = [poly(countPoly, 3), poly(countPoly, 4)];

            a = isequal(point2, check1);
            b = isequal(point2, check2);
        
            if a == 0 && b == 0;
                diff = diff +1;
            end
        end
        if diff == length(poly)
            lineIndex = countLines;     % returns index to unassigned point
            pt = 2;
            return
        end


    end

    lineIndex = 0;
    pt = 0;