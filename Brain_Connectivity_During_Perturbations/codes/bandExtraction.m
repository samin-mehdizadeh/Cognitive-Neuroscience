
EEG=pop_loadset('./Data/pullsWalk/S15.set');
tInds = find(EEG.CAT.Conn.erWinCenterTimes>=-0.5 & EEG.CAT.Conn.erWinCenterTimes<=1.5);
fThetaInds = find(EEG.CAT.Conn.freqs>=4 & EEG.CAT.Conn.freqs<=8);
fAlphaInds = find(EEG.CAT.Conn.freqs>=8 & EEG.CAT.Conn.freqs<=13);
states={'pullsStand','pullsWalk','walkRotate','standRotate'};    
for statesInds=1:4
    theta=zeros(16,16); 
    alpha=zeros(16,16);
    all=zeros(16,16);
    state=states{statesInds};
    load(['./Data/Model/' state '/ddtf_connections.mat']);
    for i=1:size(ddtf_connections,1)
        ddtf_connections{i,i}=ddtf_connections{i,i}*0;
    end
    for i=1:16
        for j=1:16
            theta(i,j) = mean(ddtf_connections{i,j}(:,fThetaInds,tInds),"all");
            alpha(i,j) = mean(ddtf_connections{i,j}(:,fAlphaInds,tInds),"all");
            all(i,j) = mean(ddtf_connections{i,j}(:,:,tInds),"all");   
         end
     end
        save(['./Data/Model/' state '/alpha.mat'],'alpha');
        save(['./Data/Model/' state '/theta.mat'],'theta');
        save(['./Data/Model/' state '/all.mat'],'all');
end

pulls_walk_alpha = load(['./Data/Model/pullsWalk/alpha.mat']).alpha;
pulls_stand_alpha = load(['./Data/Model/pullsStand/alpha.mat']).alpha;
walk_rotate_alpha = load(['./Data/Model/walkRotate/alpha.mat']).alpha;
stand_rotate_alpha = load(['./Data/Model/standRotate/alpha.mat']).alpha;
pulls_walk_theta = load(['./Data/Model/pullsWalk/theta.mat']).theta;
pulls_stand_theta = load(['./Data/Model/pullsStand/theta.mat']).theta;
walk_rotate_theta = load(['./Data/Model/walkRotate/theta.mat']).theta;
stand_rotate_theta = load(['./Data/Model/standRotate/theta.mat']).theta;
pulls_walk_all = load(['./Data/Model/pullsWalk/all.mat']).all;
pulls_stand_all = load(['./Data/Model/pullsStand/all.mat']).all;
walk_rotate_all = load(['./Data/Model/walkRotate/all.mat']).all;
stand_rotate_all = load(['./Data/Model/standRotate/all.mat']).all;
savePath = './Data/Model/Plot/bar/';
%plot a
ya = [mean(stand_rotate_theta(1:8,1:8),'ALL') mean(pulls_stand_theta(1:8,1:8),'ALL') mean(walk_rotate_theta(1:8,1:8),'ALL') mean(pulls_walk_theta(1:8,1:8),'ALL') ;
      mean(stand_rotate_alpha(1:8,1:8),'ALL') mean(pulls_stand_alpha(1:8,1:8),'ALL') mean(walk_rotate_alpha(1:8,1:8),'ALL') mean(pulls_walk_alpha(1:8,1:8),'ALL') ;
      mean(stand_rotate_all(1:8,1:8),'ALL') mean(pulls_stand_all(1:8,1:8),'ALL') mean(walk_rotate_all(1:8,1:8),'ALL') mean(pulls_walk_all(1:8,1:8),'ALL');
    ];
x = categorical({'Theta(4-8 Hz)','Alpha(8-13 Hz)','ALL(4-50 Hz)'});
x = reordercats(x,{'Theta(4-8 Hz)','Alpha(8-13 Hz)','ALL(4-50 Hz)'});
h = bar(x,ya);
set(h, {'DisplayName'}, {'StandRotate','Stand Pull','Walk Rotate','Walk Pull'}');
ylabel('dDTF')
legend()
saveas(gcf,[savePath 'cortical.png']);
%plot b
yb1 = [mean(pulls_stand_theta(9:12,9:12),'ALL') mean(pulls_walk_theta(9:12,9:12),'ALL') mean(pulls_stand_theta(9:12,12:16),'ALL') mean(pulls_walk_theta(9:12,12:16),'ALL');
     mean(pulls_stand_alpha(9:12,9:12),'ALL') mean(pulls_walk_alpha(9:12,9:12),'ALL') mean(pulls_stand_alpha(9:12,12:16),'ALL') mean(pulls_walk_alpha(9:12,12:16),'ALL');
     mean(pulls_stand_all(9:12,9:12),'ALL') mean(pulls_walk_all(9:12,9:12),'ALL') mean(pulls_stand_all(9:12,12:16),'ALL') mean(pulls_walk_all(9:12,12:16),'ALL');
    ];
yb2 = [mean(pulls_stand_theta(12:16,12:16),'ALL') mean(pulls_walk_theta(12:16,12:16),'ALL') mean(pulls_stand_theta(12:16,9:12),'ALL') mean(pulls_walk_theta(12:16,9:12),'ALL');
     mean(pulls_stand_alpha(12:16,12:16),'ALL') mean(pulls_walk_alpha(12:16,12:16),'ALL') mean(pulls_stand_alpha(12:16,9:12),'ALL') mean(pulls_walk_alpha(12:16,9:12),'ALL');
     mean(pulls_stand_all(12:16,12:16),'ALL') mean(pulls_walk_all(12:16,12:16),'ALL') mean(pulls_stand_all(12:16,9:12),'ALL') mean(pulls_walk_all(12:16,9:12),'ALL');
    ];
hc = bar(x,yb2);
set(hc, {'DisplayName'},{'Intra-leg(Stand Pull)','Intra-leg(Walk Pull)','Inter-leg(Stand Pull)','Inter-leg(Walk Pull)'}');
ylabel('dDTF')
legend()
saveas(gcf,[savePath 'muscular.png']);
%plot c
yc = [mean(pulls_stand_theta(9:16,1:8),'ALL') mean(pulls_walk_theta(9:16,1:8),'ALL') mean(pulls_stand_theta(1:8,9:16),'ALL') mean(pulls_walk_theta(1:8,9:16),'ALL');
     mean(pulls_stand_alpha(9:16,1:8),'ALL') mean(pulls_walk_alpha(9:16,1:8),'ALL') mean(pulls_stand_alpha(1:8,9:16),'ALL') mean(pulls_walk_alpha(1:8,9:16),'ALL');
     mean(pulls_stand_all(9:16,1:8),'ALL') mean(pulls_walk_all(9:16,1:8),'ALL') mean(pulls_stand_all(1:8,9:16),'ALL') mean(pulls_walk_all(1:8,9:16),'ALL');
    ];
hc = bar(x,yc);
set(hc, {'DisplayName'},{'Cortex to muscles(Stand Pull)','Cortex to muscles(Walk Pull)','Muscles to cortex(Stand Pull)',' Muscles to cortex(Walk Pull)'}');
ylabel('dDTF')
legend()
saveas(gcf,[savePath '/corticomascular.png']);