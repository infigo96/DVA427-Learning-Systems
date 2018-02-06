clear;
%clf;
clc;

A=importdata('cities.txt');
A.textdata{3,1}
C = [cell2mat(A.textdata(:,1)),cell2mat(A.textdata(:,2))]
C = arrayfun(@uint8, C);
locations = C - 64; 
inputPath = [locations, A.data]; %column 1 and 2 are the location, column 3 is the distance. 
%char(23+64) W
distanceMatrix = ones(26,26)*inf;
for i = 1:26
distanceMatrix(inputPath(i,1),inputPath(i,2)) = inputPath(i,3)
end

currentDistance = [reshape( 1:26, 26, 1), inf(26,1)]
currentDistance(6, 2) = 0;



