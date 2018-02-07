clear;
%clf;
clc;

A=importdata('cities.txt');
C = [cell2mat(A.textdata(:,1)),cell2mat(A.textdata(:,2))];
C = arrayfun(@uint8, C);
locations = C - 64; 
inputPath = [locations, A.data]; %column 1 and 2 are the location, column 3 is the distance. 
%char(23+64) W
distanceMatrix = ones(26,26)*inf;
for i = 1:length(inputPath)
distanceMatrix(inputPath(i,1),inputPath(i,2)) = inputPath(i,3); %city id 17,20&21 do not exist
distanceMatrix(inputPath(i,2),inputPath(i,1)) = inputPath(i,3); %and will be inf in the result
end %% (x,y) x is the starting location, y is the end location, the value is the travel ditance.

currentDistance =  inf(26,1);
currentDistance(6) = 0;

for iteration = 1:25
    for i = 1:26
       if currentDistance(i) ~= inf
           for j = 1:26 % too high
               if currentDistance(j) > currentDistance(i) + distanceMatrix(i,j)  
                   currentDistance(j) =  currentDistance(i) + distanceMatrix(i,j);
               end
           end
       end
    end
end
smart = double(inputPath);
G = digraph([smart(:,1), smart(:,2)],[smart(:,2),smart(:,1)],[smart(:,3),smart(:,3)]);
plot(G);
