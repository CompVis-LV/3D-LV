clear
clc

addpath(genpath('C:\Users\Jared\Documents\Thesis'))
addpath(genpath('C:\Users\Jared\Documents\ECTE458\3D-LV'))
cd C:\Users\Jared\Documents\Thesis

img = '2.png';

[lines, image] = haughTransformWORKING(img, 2, 0.5, 10, 50, 70);

linesJoined = joinVertices(lines, 50);

linesRemJoined = removeRedundant(linesJoined);

plotLines(linesRemJoined, image);
%%
polygons = [];

[lineIndex, startPoint] = unassignedPoint(linesRemJoined, polygons);

while startPoint ~= 0

    polygon = generatePolygon(linesRemJoined, lineIndex);

    validity = validatePolygon(polygon, linesRemJoined);
  
    if validity == 1
        n = nan(1,4);
        polygons = [polygons ; polygon ; n];
    end
  
    [lineIndex, startPoint] = unassignedPoint(linesRemJoined, polygons);
    if startPoint == 2
        linesRemJoined = swapEndPoints(linesRemJoined, lineIndex);
    end

        
    
end

%% Generate polygon

while p2 ~= linesRemJoined(start).point1
    
       p1 = linesRemJoined(pt).point1;
       p2 = linesRemJoined(pt).point2;
       
       lowest_angle = 360;
       
       for comp = 1:length(linesRemJoined)
           if comp ~= pt
               % Pick which route to take
               if linesRemJoined(comp).point1 == p2
                   
                   line1 = [p1; p2]
                   line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2]
                   %angle = angleBetweenLines(line1, line2)
                   angle = randi([1 359],1,1);
                   if angle < lowest_angle
                       lowest_angle = angle;
                       next = comp
                   end
                   
               elseif linesRemJoined(comp).point2 == p2
                   
                   save = linesRemJoined(comp).point2
                   linesRemJoined(comp).point2 = linesRemJoined(comp).point1
                   linesRemJoined(comp).point1 = save
                   
                   line1 = [p1; p2]
                   line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2]
                   %angle = angleBetweenLines(line1, line2)
                   angle = randi([1 359],1,1);
                   if angle < lowest_angle
                       lowest_angle = angle;
                       next = comp
                   end
               end
           end   
           
       end
       pt = next;
       polygons = [polygons ; p1 , p2]
       sides = sides + 1
       invalid = 0;

end
%% Test

test = polygons
polygons = test(1:4,:)
%%
sides = 4

%% Verify Polygon

% ** Check if polygon contains line **
           lastPolygon = polygons(end-(sides-1):end,:)
           
           % extract polygon expression
           xv = [lastPolygon(:,1)' , lastPolygon(1,1)]
           yv = [lastPolygon(:,2)' , lastPolygon(1,2)]
           
           for lines = 1:length(linesRemJoined)
               % find centre of line
               P1 = linesRemJoined(lines).point1;
               P2 = linesRemJoined(lines).point2;
               centre = (P1(:) + P2(:)).'/2
               % Does point lie within polygon
               in = inpolygon(centre(1),centre(2),xv,yv)
               if in == 1
                   % if yes set marker on
                   invalid = 1;
               end     
           end


%%  Group lines in polygons

polygons = [];
pt = 1;
polyOrigin = 1;
start = linesRemJoined(pt).point1;
error = 0;
sides = 0;

while error ~=1
    
       p1 = linesRemJoined(pt).point1;
       p2 = linesRemJoined(pt).point2;
       
       lowest_angle = 360;
       
       for comp = 1:length(linesRemJoined)
           if comp ~= pt
               % Pick which route to take
               if linesRemJoined(comp).point1 == p2
                   
                   line1 = [p1; p2]
                   line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2]
                   %angle = angleBetweenLines(line1, line2)
                   angle = randi([1 359],1,1);
                   if angle < lowest_angle
                       lowest_angle = angle;
                       next = comp
                   end
                   
               elseif linesRemJoined(comp).point2 == p2
                   
                   save = linesRemJoined(comp).point2
                   linesRemJoined(comp).point2 = linesRemJoined(comp).point1
                   linesRemJoined(comp).point1 = save
                   
                   line1 = [p1; p2]
                   line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2]
                   %angle = angleBetweenLines(line1, line2)
                   angle = randi([1 359],1,1);
                   if angle < lowest_angle
                       lowest_angle = angle;
                       next = comp
                   end
               end
           end   
           
       end
       
       pt = next;
       polygons = [polygons ; p1 , p2]
       sides = sides + 1
       invalid = 0;
       
       if p2 == start
           % ** Check if polygon contains line **
           lastPolygon = polygons(end-(sides-1):end,:)
           
           % extract polygon expression
           xv = [lastPolygon(:,1)' , lastPolygon(1,1)]
           yv = [lastPolygon(:,2)' , lastPolygon(1,2)]
           
           for lines = 1:length(linesRemJoined)
               % find centre of line
               P1 = linesRemJoined(lines).point1;
               P2 = linesRemJoined(lines).point2;
               centre = (P1(:) + P2(:)).'/2
               % Does point lie within polygon
               in = inpolygon(centre(1),centre(2),xv,yv)
               if in == 1
                   % if yes set marker on
                   invalid = 1;
               end     
           end
           
           
           %if polygon contains no lines
           if invalid == 0
               [lineIndex, point] = unassignedPoint(linesRemJoined, polygons)
               if point == 1
                   start = linesRemJoined(lineIndex).point1;
                   pt = lineIndex
                   polyOrigin = lineIndex
                   n = nan(1,4)
                   polygons = [polygons ; n]
                   sides = 0;
               elseif point == 2
                   save = linesRemJoined(lineIndex).point1;
                   linesRemJoined(lineIndex).point1 = linesRemJoined(lineIndex).point2;
                   linesRemJoined(lineIndex).point2 = save;

                   start = linesRemJoined(lineIndex).point1;
                   pt = lineIndex
                   polyOrigin = lineIndex
                   n = nan(1,4)
                   polygons = [polygons ; n]
                   sides = 0;
               else
                   a = 'return'
                   return
               end
           else
               % Return back to original point for this polygon extraction
               pt = polyOrigin;
               sides = 0;
               polygons(end-(sides-1):end,:) = [];
           end
       end
end

%%

[lineIndex, pt] = unassignedPoint(linesRemJoined, polygons)

%% pointsUnclassified
%Returns a point1 in lines which has not yet been place in a polygon 

for countLines = 1:length(lines)
    for countPoly = 1:length(poly)
        point1 = lines(countLines).point1;
        check1 = [poly(countpoly, 1), poly(countpoly, 2)]
        check2 = [poly(countpoly, 3), poly(countpoly, 4)]
        
        a = isequal(point1, check1)
        b = isequal(point1, check2)
        
        if a == 0 && b == 0
            diff = diff +1;
        end
    end
    if diff == length(poly)
        unassignedPoint = countlines      % returns index to unassigned point
        pt = 1;
        return
    end
    
    for countPoly = 1:length(poly)
        point2 = lines(countLines).point2;
        check1 = [poly(countpoly, 1), poly(countpoly, 2)]
        check2 = [poly(countpoly, 3), poly(countpoly, 4)]
        
        a = isequal(point1, check1)
        b = isequal(point1, check2)
        
        if a == 0 && b == 0
            diff = diff +1;
        end
    end
    if diff == length(poly)
        unassignedPoint = countlines;     % returns index to unassigned point
        pt = 2;
        return
    end
    

end

unassignedPoint = 0;
pt = 0;

%% TEST
sides = 5
lastPolygon = polygons(end-(sides-1):end,:)
           
% extract polygon expression
xv = [lastPolygon(:,1)' , lastPolygon(1,1)]
yv = [lastPolygon(:,2)' , lastPolygon(1,2)]

%% TEST

line1 = [linesRemJoined(1).point1; linesRemJoined(1).point2]
line2 = [linesRemJoined(7).point1; linesRemJoined(7).point2]

a1 = angleBetweenLines(line1, line2)

line1 = [linesRemJoined(1).point1; linesRemJoined(1).point2]
line2 = [linesRemJoined(9).point1; linesRemJoined(9).point2]

a2 = angleBetweenLines(line1, line2)

line1 = [linesRemJoined(7).point1; linesRemJoined(7).point2]
line2 = [linesRemJoined(9).point1; linesRemJoined(9).point2]

a3 = angleBetweenLines(line1, line2)

sum = a1 + a2 - a3
%%
clc
a = 1;

while a < length(linesRemJoined)
    
    start = linesRemJoined(a).point1;
    pt = start;
    next = linesRemJoined(a).point2;
    while next ~= start
        lowest_angle = 360
        for w = 1:length(linesRemJoined)
            if w ~= a
                if linesRemJoined(w).point1 == next
                    line1 = [linesRemJoined(w).point1; linesRemJoined(w).point2]
                    line2 = [linesRemJoined(a).point1; linesRemJoined(a).point2]
                    angle_between = angleBetweenLines(line1, line2)
                    if angle_between < lowest_angle
                        lowest_angle = angle_between;
                        next = linesRemJoined(w).point1;
                        a = a+1
                    end
                elseif linesRemJoined(w).point2 == next
                    temp = linesRemJoined(w).point2
                    linesRemJoined(w).point2 = linesRemJoined(w).point1
                    linesRemJoined(w).point1 = temp
                    
                    line1 = [linesRemJoined(w).point1; linesRemJoined(w).point2]
                    line2 = [linesRemJoined(a).point1; linesRemJoined(a).point2]
                    angle_between = angleBetweenLines(line1, line2)
                    
                    if angle_between < lowest_angle
                        lowest_angle = angle_between;
                        next = linesRemJoined(w).point1;
                        a = a+1

                    end
                end
                
            end
            
        end
        
    end
   
    
    
    
end











%%


a = vertcat(linesJoined([1:length(linesJoined)]).point1);
b = vertcat(linesJoined([1:length(linesJoined)]).point2);

points = [a;b];
points(5,1) = 2;
points(9,2) = 4;

len = 1;

while len <= length(points)
    x = sum( points(:,1)==points(len,1));
    y = sum( points(:,2)==points(len,2));
    if x == 1 || y == 1
        points(len,:) = [0, 0];
    end
    len = len + 1;
end

half = (length(points)/2);
p1 = points(1:half,:)
p2 = points((half+1):end,:)

for l = 1:length(linesJoined)
    linesJoined(l).point1 = p1(l,:)
    p1(l,:)
    linesJoined(l).point1
    linesJoined(l).point2 = p2(l,:)
    p2(l,:)
    linesJoined(l).point2
end

len = 1

while len <= length(linesJoined)
    if (linesJoined(len).point1(1,1) == 0 && linesJoined(len).point1(1,2) == 0) || ...
            (linesJoined(len).point2(1,1) == 0 && linesJoined(len).point2(1,2) == 0)
        delete = linesJoined(len)
        linesJoined(len) = [];
    end
    len = len + 1
end



%% Separate Polygons

linesSep = linesJoined

for l = 1:length(linesSep)
    
    start = linesSep(l).point1;
    
end


