cd 'C:\Users\Jared\Documents\ECTE458\3D-LV\Datasets\tPrism'
img = '18_maskedImage.png';
k = strfind(img,'_')
newStr = extractBetween(img,1,k-1)
% Perform Hough Transform and return line extracted 
[lines, image] = houghTransform(img, 4, 3, 1.6, 3, 3, 8, 20, 40);
% Join close points to form exact vertices
linesJoined = joinVertices(lines, 30);
% Remove invalid lines which contain free ends (not fixed in vertex)
linesRemJoined = removeRedundant(linesJoined);
%%
plotLines(linesRemJoined, image);
plotLines(linesJoined, image);
plotLines(lines, image);
%%
polygons = [];
% Extract ununssigned vertex (point) from object 
[lineIndex, startPoint] = unassignedPoint(linesRemJoined, polygons);
% Continues until all polygons have been found (no unassigned vertices)
while startPoint ~= 0
    % Randomly generate line path as possible polygon
    polygon = generatePolygon(linesRemJoined, lineIndex);
    % Validate polygon and check it is in simplest form
    validity = validatePolygon(polygon, linesRemJoined);
    % Store polygon data 
    if validity == 1
        n = nan(1,4);
        polygons = [polygons ; polygon ; n];
    end
    % Generate next free vertex (point) if it exists  
    [lineIndex, startPoint] = unassignedPoint(linesRemJoined, polygons);
    if startPoint == 2
        linesRemJoined = swapEndPoints(linesRemJoined, lineIndex);
    end       
    % Continues until 'unassignedPoint' returns '0' as start point
    formatSpec = 'new_points.csv';
    strp = sprintf(formatSpec,newStr{1,1});
    csvwrite(strp, polygons);
end