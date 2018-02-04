clear;
clc;
M = readtable('iris_data.csv');
irisData = importfile('iris_data.csv', 1, 150);
irisClass = M{:,5};
for i = 1:4
    irisData(:,i) = (irisData(:,i) - min(irisData(:,i)))/(max(irisData(:,i))-min(irisData(:,i)));
end
hej = arrayfun(@classname, irisClass)


function y = short(x)
    if (0 <= x) && (x <0.6)
        y = 1-1/0.6*x;

    else
     y = 0;
    end
end

function y = long(x)
    if (0.6 < x) && (x <= 1)
        y = 1/0.4*(x-0.6);

    else
     y = 0;
    end
end

function y = middle(x)
    if (0 < x) && (x < 0.6)
        y = 1/0.6*x;
    elseif (0.6 <= x) && (x < 1)
        y = 1 - 1/0.4*(x-0.6);

    else
     y = 0;
    end
end
function y = classname(x)
    if strcmp(x{1},'Iris-versicolor')
        y =1;
    elseif strcmp(x{1},'Iris-setosa')
        y = 2;
    elseif strcmp(x{1},'Iris-virginica')
        y = 3;
    else
        y = 0
    end
end

