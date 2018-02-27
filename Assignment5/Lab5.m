clc;
clear;
clf;
train = 1; %If 1 random starting position. If 0 [0 0 0 0]
startState = [0 0 0 0];
learnRate = 0.95;
toPause = 0;
learning = 1; %if have random selection of action

x3 = -pi/15:pi/30:pi/15; %theta. The angle of the pendelum.  
x4 = -pi:pi/2:pi; %theta dot. The angle velocity of the pendelum
x1 = -2.4:1.2:2.4; %x pos. The position of the cart
x2 = -10:5:10; %x dist dot. The speed of the cart

actions = [-10, 10]; % Either force backward or forward
maxEpisodes = 10000000000; %Max episodes of attempts

%rewardFunc = @(x1,x2,x3,x4)(-1.5*((abs(x3)).^2) - (0.15*(abs(x4)).^2) - (0.1*(abs(x1)).^2) - (0.05*(abs(x2)).^2));


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

 %R = rewardFunc(states(:,1),states(:,2),states(:,3),states(:,4));
 %Q = repmat(R,[1,2]);4
 Q = zeros(length(states), 2);
 if exist('SavedQ.mat', 'file') == 2
    load('SavedQ','Q')
 end
   %Initalize starting values
 currentState = startState;
 
 % Set up the pendulum plot%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
panel = figure;
panel.Position = [680 558 1000 400];
panel.Color = [1 1 1];
subplot(1,4,1)

hold on
 % Axis for the pendulum animation
f = plot(0,0,'b','LineWidth',10); % Pendulum stick
axPend = f.Parent;
axPend.XTick = []; % No axis stuff to see
axPend.YTick = [];
axPend.Visible = 'off';
axPend.Position = [0.01 0.5 0.3 0.3];
axPend.Clipping = 'off';
axis equal
axis([-1.2679 1.2679 -1 1]);
plot(0.001,0,'.k','MarkerSize',50); % Pendulum axis point

hold off
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 

for episode = 1:maxEpisodes
    if train == 0
        currentState = startState;
    elseif train == 1
        currentState = [-2.4 + (2.4+2.4)*rand, 0 ,-pi/20 + (pi/10)*rand, 0];
    end
    index = 0;

    while(abs(currentState(1)) <= 2.4 && abs(currentState(3))<=pi/15)
       index = index + 1;
    
           set(f,'XData',[0 -sin(currentState(3))]);
           set(f,'YData',[0 cos(currentState(3))]);
 
    
   [~,stateIndex] = min(sum((states - repmat(currentState,[size(states,1),1])).^2,2)); %closest state as described by our state
   %[~,actionIndex] = max(Q(stateIndex,:)); % Calculates the next action to do from Qmatrix
%    if(Q(stateIndex,1)^2/ ( Q(stateIndex,1)^2 + Q(stateIndex,2)^2) >= rand)
%        actionIndex = 1
%    else
%        actionIndex = 2
%    end
   if (rand()>0.5 && ~train)
        [~,actionIndex] = max(Q(stateIndex,:)); % Calculates the next action to do from Qmatrix
   else
       if(rand >= 0.5)
       actionIndex = 1;
       else
       actionIndex = 2;
       end
   end
 

       %[~,actionIndex] = max(Q(stateIndex,:)); % Calculates the next action to do from Qmatrix
       nextState = SimulatePendel(actions(actionIndex), currentState(1), currentState(2), currentState(3), currentState(4)); 

       [~,nextStateIndex] = min(sum((states - repmat(nextState,[size(states,1),1])).^2,2)); %closest state as described by our state
       if(learning == 1)
           %R(nextStateIndex)
           %Q(stateIndex,actionIndex) + learnRate * (R(nextStateIndex) + max(Q(nextStateIndex,:)) - Q(stateIndex,actionIndex))
           Q(stateIndex,actionIndex) = Q(stateIndex,actionIndex) + learnRate * (0.9*max(Q(nextStateIndex,:)) - Q(stateIndex,actionIndex));
          if(abs(nextState(1)) > 2.4 || abs(nextState(3))>pi/15)
          %     Q(stateIndex,actionIndex) = Q(stateIndex,actionIndex) -1;
          elseif (index > 10)
              Q(stateIndex,actionIndex) = Q(stateIndex,actionIndex) + (index^1.2)/20;
          end
       end

       currentState = nextState;
       clc;
       disp('%%%%%%%%%%%%%%%%%%%%%%%%%%');
       disp(episode)
       disp('cart distance is: ');
       disp(currentState(1));
       disp('cart speed is: ');
       disp(currentState(2));
       disp('Angle is: ');
       %disp(currentState(3));
       disp(180/pi*currentState(3));
       disp('Angle velocity is: ');
       %disp(180/pi*currentState(4));
       disp(currentState(4));
       disp('Survival time');
       disp(index*0.02);
        if (abs(currentState(1)) <= 2.4 && abs(currentState(3))<=pi/15 && index < 20000 )
                pause(toPause)
        end

    end
    if (mod(episode, 20) == 0)
        save('SavedQ','Q')
    end
   

end  % SimulatePendel(1, 1, 1, 1, 1)