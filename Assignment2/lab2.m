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
shortMatrix = arrayfun(@short, irisData);
middleMatrix = arrayfun(@middle, irisData);
longMatrix = arrayfun(@long, irisData);


%test = r1(irisData(:,i))
disp('r1 test')
for i = 1:150
    test = r1(irisData(i,:));
    if test > 0
    end
end

disp('r2 test')
for i = 1:150
    test = r2(irisData(i,:));
    if test > 0
       
    end
end

disp('r3 test')
for i = 1:150
    test = r3(irisData(i,:));
    if test > 0
        
    end
end

disp('r4 test')
for i = 1:150
    test = r4(irisData(i,:));
    if test > 0
    end
end

%classify(irisData(1,:))
%blah = arrayfun(@classify, irisData)
%classfied = zeros(length(irisData),4);
for i = 1:length(irisData)
    classified(i,:) = classify(irisData(i,:));
end

for i = 1:length(classNumber)
   Result(i,:) = classified(i,:)*classNumber(i,:)';
end
Accuracy = sum(Result)/length(Result)
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
        y =[1 0 0];
    elseif strcmp(x,'Iris-setosa')
        y = [0 1 0];
    elseif strcmp(x,'Iris-virginica')
        y = [0 0 1];
    else
        y = [-1 -1 -1];
    end
end

function y = r1(x)
if (max(short(x(1)),long(x(1))) > 0.5) && (max(middle(x(2)),long(x(2))) > 0.5) && (max(middle(x(3)),long(x(3))) > 0.5) && (middle(x(4)) > 0.5) 
    y = 1;
else
    y = 0;
end
end

function y = r2(x)
if (max(short(x(3)),middle(x(3))) > 0.5) && (short(x(4)) > 0.5) 
    y = 1;
else
    y = 0;
end
end

function y = r3(x)
if (max(short(x(2)),middle(x(2))) > 0.5) && (long(x(3)) > 0.5) && (long(x(4)) > 0.5) 
    y = 1;
else
    y = 0;
end
end

function y = r4(x)
if (middle(x(1)) > 0.5) &&(max(short(x(2)),middle(x(2))) > 0.5) && (short(x(3)) > 0.5) && (long(x(4)) > 0.5) 
    y = 1;
else
    y = 0;
end
end



function y = classify(x)
 y = [max(r1(x),r4(x)) r2(x) r3(x)];
end

