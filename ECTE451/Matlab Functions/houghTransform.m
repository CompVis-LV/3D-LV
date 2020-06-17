%%% CODE CREATED BY J. BELLINGHAM, UNIVERSITY OF WOLLONGONG %%%
% This function performs haugh transform initial pre-processing then
% generates haugh transform and identifies lines
% Lines are returned in structure array

function [lines, image] = houghTransform(img, rad, sharp, guass, a, b, N, FillGap, MinLength)
    % Read in image and convert to grayscale
    RGB = imread(img);
    A  = rgb2gray(RGB);
    image = imsharpen(A,'Radius',rad,'Amount',sharp);
    image = imdiffusefilt(image,'GradientThreshold', [a, b],'NumberOfIterations',2);
    image = imgaussfilt(A, guass);
    BW = edge(image,'canny');
    % Calculate hough transform 
    [H,theta,rho] = hough(BW);
    P = houghpeaks(H,N,'threshold',ceil(0.05*max(H(:))));
    x = theta(P(:,2));
    y = rho(P(:,1));
    % Generate lines
    lines = houghlines(BW,theta,rho,P,'FillGap',FillGap,'MinLength',MinLength);
end

