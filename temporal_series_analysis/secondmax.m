function [m,i]= secondmax(a)
b=a;
[m,i]=max(b);
b(i)=min(b);
[m,i]=max(b);
end
