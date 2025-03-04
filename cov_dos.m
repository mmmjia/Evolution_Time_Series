ins_fre=[];
site_sele=[];
ins_en=[];
ms=0;
ncut=100;
[cov_var,pair]=xlsread(['C:\Users\user\OneDrive - HKUST Connect\hilbert\cov_hilbert\',month{tt-7},'cov_hilbert.xlsx'],'Sheet1');
cov_var0=cov_var(:,1:ncut);
column_names = pair(1:ncut);
pos=1:size(column_names,2);

for site=1:size(column_names,2)
%for site=siteseta
%for site=66+36:200%66:66+36%1:66
     cov_evo=cov_var0(:,site);
     fo=emd(cov_evo(1:tt));
     if isempty(fo)==0
       [hs,f,t,imfinsf,imfinse]=hht(fo);
       
       marginal_spectrum = sum(hs, 2); 
       imfinse(:,imfinsf(tt,:)<0)=[];
       imfinsf(:,imfinsf(tt,:)<0)=[];
       imfinsf(:,imfinse(tt,:)<0.0000001)=[];
       imfinse(:,imfinse(tt,:)<0.0000001)=[];
       
       ins_en=[ins_en,imfinse(tt,:)];
       ins_fre=[ins_fre,imfinsf(tt,:)];
       [s,ss]=size(imfinsf(tt,:));
       s=pos(site)*ones([1,ss]);
       site_sele=[site_sele,s];
       ms=ms+marginal_spectrum;

     end
     
end
edges = linspace(0, 3, 100);
%histogram(ins_fre,edges);
%xlim([0,3])
%xlabel('f (frequency)','FontSize', 15)
%ylabel('number of modes','FontSize', 15)
[f0,x]=ksdensity(ins_fre,'Bandwidth',0.08);