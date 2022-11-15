states={'pullsStand','pullsWalk','walkRotate','standRotate'};
parts={'EMG','Brain'};
timelim = [-0.5 1.5];
freqlim = [4 50];
brainLabels = {'Left Occipital','Right Occipital','Left Sensorimotor','Anterior Cingulate','Right Sensorimotor','Posterior Parietal','Supplementary Motor Area','Anterior Parietal'};
emgLabels = {'Left Tibialis Anterior','Left Soleus','Left Medial Gastrocenemius','Left Peroneus Longus','Right Tibialis Anterior','Right Soleus','Right  Medial Gastrocenemius','Right Peroneus Longus'};
savePath = './Data/Model/plot/';
for statesInds=1:4
    for partsInds=1:2
        state=states{statesInds};
        part=parts{partsInds};
        load(['./Data/Model/' state '/baseSub_Connections.mat']);
        EEG=pop_loadset('./Data/pullsStand/S1.set');
        for channel = 1:8
            if strcmp(part,'Brain')
                conn = baseSub_Connections(1:8,1:8,:,:);
                labelName = brainLabels{channel};
            else
                conn = baseSub_Connections(9:16,9:16,:,:);
                labelName = emgLabels{channel};
            end
            alltimes = EEG.CAT.Conn.erWinCenterTimes;
            allfreqs = EEG.CAT.Conn.freqs;
            tftopo(squeeze(conn(channel,channel,:,:)),alltimes,allfreqs,'vert',[],'limits',[timelim freqlim],'logfreq','native')
            title(labelName);
            saveas(gcf,[savePath state '/' part '/' labelName '.png']);
        end
    end
end