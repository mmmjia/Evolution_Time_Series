function [siter]=oringnal_data2(site,tt)
path="D://spyder-tensor//mutation_aa//all//.xlsx";
pathnew=insertAfter(path,"all//",string(site));
ssite=readmatrix(pathnew);
ssite(:,1)=[];
ssite(1,:)=[];
m=[];
[n,s]=sort(ssite(tt,:));
ssite1=ssite(1:tt,s(end));
m=ssite(1:tt,s(end-1));
m2=ssite(1:tt,s(end-2));
siter=[ssite1';m';m2'];
end
