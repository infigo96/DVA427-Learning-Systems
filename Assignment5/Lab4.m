clc;
clear;

startState = [0 0 0 0];

x1 = -pi/6:0.5:pi/6; %theta. THe angle of the pendelum.
x2 = -pi:0.1:pi; %theta dot. The angle velocity of the pendelum
x3 = -2.4:0.1:2.4; %x pos. The position of the cart
x4 = -10:1:10; %x dist dot. The speed of the cart
% x1 = -pi/6:pi/6:pi/6; %theta. THe angle of the pendelum.
% x2 = -pi:pi:pi; %theta dot. The angle velocity of the pendelum
% x3 = -2.4:2.4:2.4; %x pos. The position of the cart
% x4 = -10:10:10; %x dist dot. The speed of the cart
actions = [-10, 10]; % Either force backward or forward
maxEpisodes = 100; %Max episodes of attempts

rewardFunc = @(x1,x2,x3,x4)(-1*((abs(x1)).^2) - (0.2*(abs(x2)).^2) - (0.1*(abs(x3)).^2) - (0.02*(abs(x4)).^2));


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

 R = rewardFunc(states(:,1),states(:,2),states(:,3),states(:,4));
 Q = repmat(R,[1,2]);
 
   %Initalize starting values
 currentState = startState;
 

for episode = 1:maxEpisodes
 
    
   [~,stateIndex] = min(sum((states - repmat(currentState,[size(states,1),1])).^2,2));
 
   [~,actionIndex] = max(Q(stateIndex,:));

end  % SimulatePendel(1, 1, 1, 1, 1)