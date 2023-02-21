n=size(siteseta,2);
%tt=9;
ifnall=[];
pos=[];
site=[];
oder=[];
for i=1:n
    siter=oringnal_data(siteseta(i));
    site1=siter(1,1:tt);
    site2=siter(2,1:tt);
    site3=siter(3,1:tt);
    fo=emd(site1);
    ifnall2=[];
    if isempty(fo)==0
        [hs,f,t,imfinsf,imfinse]=hht(fo);
        imfinsf(:,imfinsf(tt,:)<0)=[];
        [s,ss]=size(imfinsf);
        [aa,bb]=max(imfinsf(tt,:));
        if ss>1 %&& aa>1.5
            ss=ss-1;
            imfinsf(:,bb)=[];        
        end
        ifnall2=imfinsf;
        oder=[oder,ones([1,ss])];
        %site=[site,siteseta(i)];
    end
    if site2(tt)>0.3*site1(tt)
        fo=emd(site2);
        %[s,ss]=size(fo);
        if isempty(fo)==0
            [hs,f,t,imfinsf,imfinse]=hht(fo);
            imfinsf(:,imfinsf(tt,:)<0)=[];
            [s,ss]=size(imfinsf);
            [aa,bb]=max(imfinsf(tt,:));
            if ss>1% && aa>1.5
               ss=ss-1;
               imfinsf(:,bb)=[];        
            end
            ifnall2=[ifnall2,imfinsf];
            oder=[oder,2*ones([1,ss])];
            %site=[site,siteseta(i)];
        end
    end
    if site3(tt)>site2(tt)
        if isempty(fo)==0
            [hs,f,t,imfinsf,imfinse]=hht(fo);
            ifnall2=[ifnall2,imfinsf];
            %site=[site,siteseta(i)];
        end
    end
    %if isempty(ifnall2)==0 && sum(ifnall2(tt,:)>a0 &ifnall2(tt,:)<b)>0
        %pos=[i,pos];
     %   pos=[siteseta(i),pos];
    %end
    %ifnall2(ifnall2>2.5)=[];
    [s,ss]=size(ifnall2);
    s=siteseta(i)*ones([1,ss]);
    site=[site,s];
    %(ifnall2(tt,:))
    ifnall=[ifnall,ifnall2];
end
edges = linspace(0, 3, 80);
pt=histogram(ifnall(tt,:),edges);
xlim([0,3])
xlabel('f (frequency)','FontSize', 15)
ylabel('number of modes','FontSize', 15)
unique(pos);
%title('2020-09','FontSize',15)