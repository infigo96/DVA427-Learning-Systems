clear;
clc;
M = readtable('iris_data.csv');
irisData = importfile('iris_data.csv', 1, 150);
irisClass = M{:,5};
for i = 1:4
    irisData(:,i) = (irisData(:,i) - min(irisData(:,i)))/(max(irisData(:,i))-min(irisData(:,i)));
end
for i = 1:length(irisClass)
    classNumber(i,:) = classname(irisClass{i});
end

%short(irisData(:,1))
% shortMatrix = arrayfun(@short, irisData);
% middleMatrix = arrayfun(@middle, irisData);
% longMatrix = arrayfun(@long, irisData);



for i = 1:length(irisData)
    classified(i,:) = classify(irisData(i,:));
end

for i = 1:length(classNumber)
    if classified(i,1) == classNumber(i,1)
        Result(i,:) = 1;
    else 
        Result(i,:) = 0;
    end
end
Accuracy = sum(Result)/length(Result)

%-------------------------------------Functions--------------
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
    if strcmp(x,'Iris-versicolor')
        y =1;
    elseif strcmp(x,'Iris-setosa')
        y = 2;
    elseif strcmp(x,'Iris-virginica')
        y = 3;
    else
        y = -1;
    end
end

function y = r1(x)
y = min([max(short(x(1)),long(x(1))) , max(middle(x(2)),long(x(2))), max(middle(x(3)),long(x(3))) , middle(x(4))]);

end

function y = r2(x)
y = min([max(short(x(3)),middle(x(3))) ,short(x(4))]);
 
end

function y = r3(x)
y = min([max(short(x(2)),middle(x(2))) , long(x(3)) , long(x(4))]);
 
end

function y = r4(x)
y = min([middle(x(1)) , max(short(x(2)),middle(x(2))) , short(x(3)) , long(x(4))]);

end



function y = classify(x)
 t = [r1(x) r2(x) r3(x) r4(x)];
 m = max(t);
 if t(1) == m || t(4) == m
     y = 1;
 elseif t(2) == m
     y = 2;
 elseif t(3) == m
     y = 3;
 end
end

