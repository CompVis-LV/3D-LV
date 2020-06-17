%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function swaps the end points of a line

function lines = swapEndPoints(lines, index)
    store = lines(index).point2;
    lines(index).point2 = lines(index).point1;
    lines(index).point1 = store;
end