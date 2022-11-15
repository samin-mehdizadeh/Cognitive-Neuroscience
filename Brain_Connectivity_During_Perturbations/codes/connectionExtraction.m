RootData='./Data/';
savePath='./Data/Model/';
states={'pullsStand','pullsWalk','walkRotate','standRotate'};
for stateIdx=1:length(states)
    alpha = 0.05; 
    state=states{stateIdx};
    [spectral_connections,ddtf_connections] = find_all_connections(state);
    save(['./Data/Model/' state '/ddtf_connections.mat'],'ddtf_connections');
    save(['./Data/Model/' state '/spectral_connections.mat'],'spectral_connections');
    baseSub_Connections = zeros(16,16,30,244);
    times=EEG.CAT.Conn.erWinCenterTimes;
    baseidx=find(times>=-0.5 & times<=0);
    for j=1:16
        for k=1:16
            baseVals=median(spectral_connections{j,k}(:,:,baseidx),3);
            curr_ersp = spectral_connections{j,k}-repmat(baseVals, [1, 1, length(times)]);
            curr_ersp=permute(curr_ersp,[2 3 1]);
                pboot = bootstat(curr_ersp,'median(arg1,3);','boottype','shuffle',...
                    'label','ERSP','bootside','both','naccu',200,...
                    'basevect',baseidx,'alpha',alpha,'dimaccu',2);
                curr_ersp = median(curr_ersp,3);
                curr_maskedersp = curr_ersp;
                curr_maskedersp(curr_ersp > repmat(pboot(:,1),[1 size(curr_ersp,2)]) & curr_ersp < repmat(pboot(:,2),[1 size(curr_ersp,2)])) = 0;
            curr_maskedersp=permute(curr_maskedersp,[3 1 2]);
            baseSub_Connections(j,k,:,:)=squeeze(curr_maskedersp);
        end
    end
    save(['./Data/Model/' state '/baseSub_Connections.mat'],'baseSub_Connections');
end
%%
function [spectral_connections,ddtf_connections] = find_all_connections(state)
    valid_clusters=3:10; %clusterNums;
    cluster_data=load('./Data/cluster_1222018.mat').cluster; 
    subjectInds=[1:7 9:13 15:17 19:20 22:33];
    subjects=[1:13 15:17 19:20 22:33];
    ddtf_connections=cell(16,16);
    spectral_connections=cell(16,16);
    num_connections=zeros(16,16);
    for subject=subjectInds
        EEG=pop_loadset('filename', ['S' num2str(subject) '.set'], 'filepath', ['./Data/' state]);
        subject_channels=[];
        for i=1:length(valid_clusters)
            if any(subjects(cluster_data(valid_clusters(i)).sets)==subject)
                subject_channels=[subject_channels i];
            end
        end
        subject_channels=[subject_channels 9:16]; 
        num_connections(subject_channels,subject_channels)=num_connections(subject_channels,subject_channels)+1;
        for j=1:length(subject_channels)
            for k=1:length(subject_channels)
                ddtf_connections{subject_channels(j),subject_channels(k)}(num_connections(subject_channels(j),subject_channels(k)),:,:)=squeeze(EEG.CAT.Conn.dDTF08(j,k,:,:));
                spectral_connections{subject_channels(j),subject_channels(k)}(num_connections(subject_channels(j),subject_channels(k)),:,:)=squeeze(EEG.CAT.Conn.S(j,k,:,:));
            end
        end 
    end
end
