

function linesJoined = joinVertices(lines, range)
    a = vertcat(lines([1:length(lines)]).point1);
    b = vertcat(lines([1:length(lines)]).point2);

    points = [a;b];


    for l = 1:length(points)
        a = l;

        Idx = rangesearch(points,points(l,:), range);

        d = Idx{1};


        num = length(d);

        X = 0; Y = 0;
        for c = 1:num
        X = points(d(c),1) + X;
        Y = points(d(c),2) + Y;
        end
        Xav = X/num;
        Yav = Y/num;

        for c = 1:num
        points(d(c),:) = [Xav, Yav]
        end 

    end

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