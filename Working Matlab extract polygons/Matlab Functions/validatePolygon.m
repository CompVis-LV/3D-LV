% Validate that generated polygon is of most simple form given lines
% available. That is no lines from 'lines' fit inside polygon


function validity = validatePolygon(polygon, lines)

validity = 1;
           

           % extract polygon expression
           xv = [polygon(:,1)' , polygon(end,3)]
           yv = [polygon(:,2)' , polygon(end,4)]
           
           p = polyshape(xv,yv,'Simplify',false)
           validity = issimplified(p)
           
           for lineCount = 1:length(lines)
               % find centre of line
               P1 = lines(lineCount).point1;
               P2 = lines(lineCount).point2;
               
               centre = (P1(:) + P2(:)).'/2;
               % Does point lie within polygon
               in1 = inpolygon(centre(1)+1,centre(2),xv,yv);
               in2 = inpolygon(centre(1),centre(2)+1,xv,yv);
               in3 = inpolygon(centre(1)-1,centre(2),xv,yv);
               in4 = inpolygon(centre(1),centre(2)-1,xv,yv);
               in5 = inpolygon(centre(1),centre(2),xv,yv);
               if in1 == 1 && in2 == 1 && in3 == 1 && in4 == 1 && in5 == 1
                   % if yes set marker on
                   validity = 0;
                   return
               end     
           end


end
