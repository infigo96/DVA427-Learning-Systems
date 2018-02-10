clear;
%clf;
clc;
 % Fix path finding
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

pathTo{26} = []; %VERY IMPORTANT TO DO, else everything will be undefined thus crash and burn
pathTo{6} = [6]; % The path to point 6 is 6

for iteration = 1:25
    for i = 1:26 % This is the inner node
       if currentDistance(i) ~= inf %if outter node has not a distance to itself it can't be reached yet
           for j = 1:26 % too high? j is the outter node 
               if currentDistance(j) > currentDistance(i) + distanceMatrix(i,j)
                   pathTo{j} = [pathTo{i}, j];  %new path = the better Path + to the node
                   currentDistance(j) =  currentDistance(i) + distanceMatrix(i,j);
               end
           end
       end
    end
end
disp(currentDistance)
smart = double(inputPath);
G = digraph([smart(:,1), smart(:,2)],[smart(:,2),smart(:,1)],[smart(:,3),smart(:,3)]);
plot(G);
