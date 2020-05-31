%% Functions


function [lines, image] = haughTransform(img, rad, sharp, N, FillGap, MinLength)

    RGB = imread(img);
    A  = rgb2gray(RGB);

    image = imsharpen(A,'Radius',rad,'Amount',sharp);

    BW = edge(image,'canny');

    [H,theta,rho] = hough(BW);

    P = houghpeaks(H,N,'threshold',ceil(0.1*max(H(:))));

    x = theta(P(:,2));
    y = rho(P(:,1));

    lines = houghlines(BW,theta,rho,P,'FillGap',FillGap,'MinLength',MinLength);

end

