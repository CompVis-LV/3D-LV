%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function takes standard lines structure and joins lines whos ends
% are close together to form vertices. 

function linesJoined = joinVertices(lines, range)
    % create easy to work with array
    a = vertcat(lines([1:length(lines)]).point1);
    b = vertcat(lines([1:length(lines)]).point2);
    points = [a;b];
    for l = 1:length(points)
        % find points that are withing Euclidean distance 'range' from
        Idx = rangesearch(points,points(l,:), range);
        d = Idx{1};
        num = length(d);
        % Calculate centre between two close points
        X = 0; Y = 0;
        for c = 1:num
        X = points(d(c),1) + X;
        Y = points(d(c),2) + Y;
        end
        Xav = X/num;
        Yav = Y/num;
        % modify points
        for c = 1:num
        points(d(c),:) = [Xav, Yav]
        end 
    end
    % Edit lines structure to reflect new line end points
    half = (length(points)/2);
    p1 = points(1:half,:)
    p2 = points((half+1):end,:)
    linesJoined = lines;
    for l = 1:length(linesJoined)
        linesJoined(l).point1 = p1(l,:)
        p1(l,:)
        linesJoined(l).point1
        linesJoined(l).point2 = p2(l,:)
        p2(l,:)
        linesJoined(l).point2
    end
end