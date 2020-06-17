%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function remove redundant lines from shape
% These are duplicate lines, or lines that have free ends (therefore do not
% create a valid polygon 

function linesJoined = removeRedundant(linesJoined)
    % If two lines are equal remove one
    j = 1; k = 1;
    while j <= length(linesJoined)
        k = 1;
        while k <= length(linesJoined)
            if j ~= k
                a = isequal(linesJoined(j).point1, linesJoined(k).point1)
                b = isequal(linesJoined(j).point2, linesJoined(k).point2)
                c = isequal(linesJoined(j).point1, linesJoined(k).point2)
                d = isequal(linesJoined(j).point2, linesJoined(k).point1)
                if (a == 1 && b == 1) || (c == 1 && d == 1)
                    linesJoined(k) = [];
                    j = 0; k = 1; break
                end
            end
            k = k + 1;  
        end
        j = j + 1;
    end
    % Changes formate to simple array
    a = vertcat(linesJoined([1:length(linesJoined)]).point1);
    b = vertcat(linesJoined([1:length(linesJoined)]).point2);
    points = [a;b];
    len = 1;
    % Sets all invalid points to origin, Implementation assumes no image 
    % will be cropped to the corner of a shape. 
    while len <= length(points)
        x = sum(points(:,1)==points(len,1));
        y = sum(points(:,2)==points(len,2));
        % Check if any points only occur once (lines with free end)
        if (x == 1 || y == 1) && (points(len,1) ~= 0 && points(len,2) ~= 0)
            points(len,:) = [0,0];
            % remove also other endpoint of free line
            h = length(points)/2;
            if len <= h
                points(len+h,:) = [0,0];
            else
                points(len-h,:) = [0,0];
            end
            len = 0;
        end
        len = len + 1
    end
    % transfer infomation to line structure
    half = (length(points)/2);
    p1 = points(1:half,:)
    p2 = points((half+1):end,:)
    for l = 1:length(linesJoined)
        linesJoined(l).point1 = p1(l,:);
        linesJoined(l).point2 = p2(l,:);
    end
    % Remove all invalid points
    len = 1;
    while len <= length(linesJoined)
        if (linesJoined(len).point1(1,1) == 0 && ...
                linesJoined(len).point1(1,2) == 0) || ...
                (linesJoined(len).point2(1,1) == 0 && ...
                linesJoined(len).point2(1,2) == 0)
            linesJoined(len) = [];
            len = 0;
        end
        len = len + 1;
    end
end
