clc;
clear;

x1 = -pi/6:0.5:pi/6; %theta. THe angle of the pendelum.
x2 = -pi:0.1:pi; %theta dot. The angle velocity of the pendelum
x3 = -2.4:0.1:2.4; %x pos. The position of the cart
x4 = -10:1:10; %x dist dot. The speed of the cart
actions = [-10, 10]; % Either force backward or forward
maxEpisodes = 100; %Max episodes of attempts

%What do we need?
    %Current states
    %Reward function
    %Qmatrix
    index = 1;
 for i=1:length(x1)   
    for j=1:length(x2)
        for k = 1:length(x3)
            for l = 1:length(x4)
                states(index,1)=x1(i);
                states(index,2)=x2(j);
                states(index,3)=x3(k);
                states(index,4)=x4(l);
                index=index+1;
            end
        end
    end
 end

for episode = 1:maxEpisodes
    
   % SimulatePendel(1, 1, 1, 1, 1)

end