function [siter]=oringnal_data(site)
path="D://spyder-tensor//mutation_aa//all//.xlsx";
pathnew=insertAfter(path,"all//",string(site));
ssite=readmatrix(pathnew);
ssite(:,1)=[];
ssite(1,:)=[];
m=[];
for i =1:31
[A,~]=sort(ssite(i,:));
m=[m,A(end-1)];
end
m2=[];
for i =1:31
[A,~]=sort(ssite(i,:));
m2=[m2,A(end-2)];
end
ssite1=(max(ssite'));
siter=[ssite1;m;m2];
end
