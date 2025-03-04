%save_voi.f=[];
%save_voi.x=[];
%save_voi.ms=[];
%save_voi.f0=[];
%save_voi.sitef=[];
%save_voi.site_order=[];

for tt=12:20
cov_pair_var
save_voi(tt-7).f=f;
save_voi(tt-7).x=x;
save_voi(tt-7).ms=ms;
save_voi(tt-7).f0=f0;
save_voi(tt-7).sitef=ins_fre;
save_voi(tt-7).site_order=site_sele;
end

 hold off
for tt=12:20
fill(save_voi(tt-7).x,-0.5*save_voi(tt-7).f0+tt,[0,1,1])
hold on
end