
% Generate random polygon from lines given starting point

function [polygon] = generatePolygon(linesRemJoined, pt)

    p2 = 0;
    sides = 0;
    start = pt;
    polygon = [];

    while p2 ~= linesRemJoined(start).point1

           p1 = linesRemJoined(pt).point1;
           p2 = linesRemJoined(pt).point2;

           lowest_angle = 360;

           for comp = 1:length(linesRemJoined)
               if comp ~= pt
                   % Pick which route to take
                   if linesRemJoined(comp).point1 == p2

                       %line1 = [p1; p2];
                       %line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2];
                       %angle = angleBetweenLines(line1, line2)
                       angle = randi([1 359],1,1);
                       if (angle < lowest_angle)
                           lowest_angle = angle;
                           next = comp;
                       end

                   elseif linesRemJoined(comp).point2 == p2

                       save = linesRemJoined(comp).point2;
                       linesRemJoined(comp).point2 = linesRemJoined(comp).point1;
                       linesRemJoined(comp).point1 = save;

                       %line1 = [p1; p2];
                       %line2 = [linesRemJoined(comp).point1; linesRemJoined(comp).point2];
                       %angle = angleBetweenLines(line1, line2)
                       angle = randi([1 359],1,1);
                       if angle < lowest_angle
                           lowest_angle = angle;
                           next = comp;
                       end
                   end
               end   

           end
%            skip = 0;
%            a = [linesRemJoined(next).point1, linesRemJoined(next).point2];
%            if size(polygon,1) > 0
%                for L = size(polygon,1)
%                    if a == polygon(L,:)
%                        skip = 1
%                    end
%                end
%            end
%            if skip ~= 1           
%                pt = next;
%                polygon = [polygon ; p1 , p2];
%            end
                pt = next;
                polygon = [polygon ; p1 , p2];
    end
     
end
