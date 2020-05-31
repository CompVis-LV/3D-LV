

function lines = removeRedundant(linesJoined)

% Add if two lines are equal remove one

    a = vertcat(linesJoined([1:length(linesJoined)]).point1);
    b = vertcat(linesJoined([1:length(linesJoined)]).point2);

    points = [a;b];
    %points(5,1) = 2;
    %points(9,2) = 4;

    len = 1;

    while len <= length(points)
        x = sum( points(:,1)==points(len,1));
        y = sum( points(:,2)==points(len,2));
        if (x == 1 || y == 1) && (points(len,1) ~= 0 && points(len,2) ~= 0)
            points(len,:) = [0,0];
            len = 1;
        end
        len = len + 1;
    end

    half = (length(points)/2);
    p1 = points(1:half,:);
    p2 = points((half+1):end,:);
    

    for l = 1:length(linesJoined)
        linesJoined(l).point1 = p1(l,:);
        %p1(l,:)
        %linesJoined(l).point1
        linesJoined(l).point2 = p2(l,:);
        %p2(l,:)
        %linesJoined(l).point2
    end

    len = 1;

    while len <= length(linesJoined)
        if (linesJoined(len).point1(1,1) == 0 && linesJoined(len).point1(1,2) == 0) || ...
                (linesJoined(len).point2(1,1) == 0 && linesJoined(len).point2(1,2) == 0);
            %delete = linesJoined(len);
            linesJoined(len) = [];
            len = 1;
        end
        len = len + 1;
    end
    
lines = linesJoined;

end
