n=size(siteseta,2);
a=zeros(n);
for i =1:n
[hs,hs1,f,t,imfinsfi,imfinse,ssite] =hilemd(siteseta(i),1,tt);
imfinsfi(:,find(imfinse(tt,:)<0.1))=[];
for j = 1:n
[hs,hs1,f,t,imfinsfj,imfinse,ssite] =hilemd(siteseta(j),1,tt);
imfinsfj(:,find(imfinse(tt,:)<0.1))=[];
kk=[];
for k=1:size(imfinsfi,2)
for m=1:size(imfinsfj,2)
dis=0;  
dis=abs(imfinsfi(end,k)-imfinsfj(end,m));
dis=dis+abs(imfinsfi(end-1,k)-imfinsfj(end-1,m));
dis=dis+abs(imfinsfi(end-2,k)-imfinsfj(end-2,m));
%dis=dis+abs(imfinsfi(end-3,k)-imfinsfj(end-3,m));
%dis=dis+abs(imfinsfi(end-4,k)-imfinsfj(end-4,m));
%dis=abs(imfinsfi(end,k)-imfinsfj(end,m)-imfinsfi(end-1,k)+imfinsfj(end-1,m));
kk=[kk,dis];
end
end
a(i,j)=min(kk);
end
end
%a(a>0.15)=nan;
imagesc(-a)
xx=1:n;xticks(xx)
yticks(xx)
yticklabels(siteseta)
xticklabels(siteseta)
colorbar
caxis([-0.12 0])
