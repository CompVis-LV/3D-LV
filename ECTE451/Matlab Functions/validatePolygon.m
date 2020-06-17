%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function is used to validate that generated polygon is of most 
% simple form given lines available.

function validity = validatePolygon(polygon, lines)
    % Initiate, returns true if no 
    validity = 1;          
    % Extract polygon expression
    xv = [polygon(:,1)' , polygon(end,3)]
    yv = [polygon(:,2)' , polygon(end,4)]
    % Test whether shape is a well-defined polygon, matlab function
    p = polyshape(xv,yv,'Simplify',false)
    validity = issimplified(p)
    % for all possible lines in 3D shape
    for lineCount = 1:length(lines)
        % find centre of line
        P1 = lines(lineCount).point1;
        P2 = lines(lineCount).point2;
        % find centre of line
        centre = (P1(:) + P2(:)).'/2;
        % Does point lie within polygon
        % As rounding errors occur leading to false negatives, we
        % test points, 1 unit from centre in all 4 direction
        in1 = inpolygon(centre(1)+1,centre(2),xv,yv);
        in2 = inpolygon(centre(1),centre(2)+1,xv,yv);
        in3 = inpolygon(centre(1)-1,centre(2),xv,yv);
        in4 = inpolygon(centre(1),centre(2)-1,xv,yv);
        in5 = inpolygon(centre(1),centre(2),xv,yv);
        % All points must fall inside the polygon to invalidate
        if in1 == 1 && in2 == 1 && in3 == 1 && in4 == 1 && in5 == 1
            % if yes set marker on
            validity = 0;
            return
        end     
    end
end
