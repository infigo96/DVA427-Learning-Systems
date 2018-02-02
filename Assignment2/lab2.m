clear;
clc;
M = readtable('iris_data.csv');

irisData = importfile('iris_data.csv', 1, 150);
irisClass = M{:,5}
irisData(:,1) = (irisData(:,1) - min(irisData(:,1)))/(max(irisData(:,1))-min(irisData(:,1)))
