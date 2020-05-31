
function lines = swapEndPoints(lines, index)


    save = lines(index).point2;
    lines(index).point2 = lines(index).point1;
    lines(index).point1 = save;


end