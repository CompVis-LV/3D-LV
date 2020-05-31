

function plotLines(lines, I)

    figure, imshow(I), hold on
    max_len = 0;
    for k = 1:length(lines)

       xy = [lines(k).point1; lines(k).point2];

       plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

       plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
       plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');

    end

end