clear;
clc;
M = readtable('iris_data.csv');
irisData = importfile('iris_data.csv', 1, 150);
irisClass = M{:,5};
for i = 1:4 %Normelizeing of each data type (column)
    irisData(:,i) = (irisData(:,i) - min(irisData(:,i)))/(max(irisData(:,i))-min(irisData(:,i)));
end
for i = 1:length(irisClass)%Defines a number for the class name. 
    classNumber(i,:) = classname(irisClass{i});
end


for i = 1:length(irisData) %Classify each Test case and fills the return in a vector.
    classified(i,:) = classify(irisData(i,:));
end

for i = 1:length(classNumber)%Compares each test case with the correct result.
    if classified(i,1) == classNumber(i,1)
        Result(i,:) = 1;
    else 
        Result(i,:) = 0;
    end
end
Accuracy = sum(Result)/length(Result)%The % of the testcases that was classified correctly.

%-------------------------------------Functions--------------
function y = short(x) %Membership function of short
    if (0 <= x) && (x <0.6)
        y = 1-1/0.6*x;

    else
     y = 0;
    end
end

function y = long(x) %Membership function of long
    if (0.6 < x) && (x <= 1)
        y = 1/0.4*(x-0.6);

    else
     y = 0;
    end
end

function y = middle(x) %Membership function of middle
    if (0 < x) && (x < 0.6)
        y = 1/0.6*x;
    elseif (0.6 <= x) && (x < 1)
        y = 1 - 1/0.4*(x-0.6);
    else
     y = 0;
    end
end
function y = classname(x) %Returns a number correlating to the input string
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

function y = r1(x)%Fuzzy class degree for r1 (versicolor 1)
y = min([max(short(x(1)),long(x(1))) , max(middle(x(2)),long(x(2))), max(middle(x(3)),long(x(3))) , middle(x(4))]);

end

function y = r2(x) %Fuzzy classification for  r2 (setosa)
y = min([max(short(x(3)),middle(x(3))) ,short(x(4))]);
 
end

function y = r3(x) %Fuzzy class degree for r3 (virginica)
y = min([max(short(x(2)),middle(x(2))) , long(x(3)) , long(x(4))]);
 
end

function y = r4(x) %Fuzzy class degree for r4 (versicolor 2)
y = min([middle(x(1)) , max(short(x(2)),middle(x(2))) , short(x(3)) , long(x(4))]);

end



function y = classify(x) %Selects the class the test case belongs to
 t = [r1(x) r2(x) r3(x) r4(x)]; %A vector for the different classes degrees
 m = max(t); 
 if t(1) == m || t(4) == m %choose the one that was the largest one (most likely) 
     y = 1;
 elseif t(2) == m
     y = 2;
 elseif t(3) == m
     y = 3;
 end
end

