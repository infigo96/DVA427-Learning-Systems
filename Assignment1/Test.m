A=importdata('C:\Users\hampu\Downloads\assignment 1 titanic.dat');
B = A.data;
F = B(:,1:3);
G = B(:,4);
rub;
alive = 0;
dead = 0;
survcorr = 0;
deathcorr = 0;
for i = 1500:2200
    if (G(i,1) == 1)
        alive = alive +1;
        if(net(F(i,:)') >= 0.5)
            survcorr = survcorr +1;
        end
    else
        dead = dead +1;
        if(net(F(i,:)') < 0.5)
            deathcorr = deathcorr +1;
        end
    end
end
procc =survcorr/alive
doccc = deathcorr/dead
all = (survcorr+deathcorr)/(alive + dead)