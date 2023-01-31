function [hs,hs1,f,t,inf,infe,ssite] = hilemd(site,t0,t1)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
path="D://spyder-tensor//mutation_aa//all//.xlsx";
pathnew=insertAfter(path,"all//",string(site));
ssite=readmatrix(pathnew);
ssite(:,1)=[];
ssite(1,:)=[];
inf=[];
m=[];
hs1=0;
for i =1:24
[A,pos]=sort(ssite(i,:));
m=[m,A(end-1)];
end
m2=[];
for i =1:24
[A,pos]=sort(ssite(i,:));
m2=[m2,A(end-2)];
end
ssite1=(max(ssite'));
[n,s]=max(ssite(t1,:));
%ssite1=ssite(1:t1,s)';
fo=emd(ssite1(t0:t1));
if isempty(fo)==0
[hs,f,t,imfinsf,imfinse]=hht(fo);
end
ssite12=m';
fo=emd(ssite12(t0:t1));
if ssite12(t1)>0.3*ssite1(t1) && isempty(fo)==0
    infe=imfinse;
    inf=imfinsf;
    [nn,ss]=secondmax(ssite(t1,:));
    %ssite1=ssite(1:t1,ss)';
    [hs1,f,t,imfinsf,imfinse]=hht(fo);
    inf=[inf,imfinsf];
    infe=[infe,imfinse];
   % if m2(t1)>m(t1)
    %    ssite1=m2';
     %   [hs,f,t,imfinsf,imfinse]=hht(emd(ssite1(t0:t1)));
      %  inf=[inf,imfinsf];
       % infe=[infe,imfinse];
    %end
else        
    inf=imfinsf;
    infe=imfinse;
%ssite1=(max(ssite'));
%ssite1=sum(ssite')-(max(ssite'))-m';
%ssite1=sum(ssite');
end
end

