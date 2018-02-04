clear;
clc;
M = readtable('iris_data.csv');

irisData = importfile('iris_data.csv', 1, 150);
irisClass = M{:,5};
for i = 1:4
    irisData(:,i) = (irisData(:,i) - min(irisData(:,i)))/(max(irisData(:,i))-min(irisData(:,i)));
end
