# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:08:08 2025

@author: user
"""

import pandas as pd
import numpy as np
import sys
import os

path0='C:/Users/user/OneDrive - HKUST Connect/cleanproteindata/'
folder_path = 'C:/Users/user/OneDrive - HKUST Connect/hilbert/cov_hilbert_sele_pairs/'



year = ['2020','2021','2022','2023']; months = [str(i).zfill(2) for i in range(1,12+1)]
month0 = [i+'-'+j for i in year for j in months]
m=200

alpha=[144, 501, 570, 716, 982, 1118, 69, 70, 681, 614]
beta=[80, 215, 241, 242, 243, 417, 484, 501, 701,614]
gamma= [18, 20, 26, 138, 190, 417, 484, 501, 614, 655, 1027, 1176,614]
lammbda=[75, 76, 246, 247, 248, 249, 250, 251, 252, 253, 490, 614, 859,614]
delta=[ 19, 156, 157, 158, 452, 478, 950,614]
omicron=[ 67, 69, 70, 95, 143, 144, 145, 211, 212, 339, 371, 373, 375, 417,
         440, 446, 477, 484, 493, 496, 498, 501, 505, 547, 655, 679, 764, 796, 
         856, 954, 969, 981]

class Pair_cov:
    def __init__(self,name,cov,col):
        self.name=name
        self.cov=cov
        self.col=col

def get_pair_cov(site,save_name):
    n_group=len(site)

    cor_all=[]
    for k in range(n_group):
        n=len(site[k])
        cor_time=np.zeros((48,int(n*(n-1)/2)))
        cor_all.append(Pair_cov(save_name[k], cor_time,[0]*int(n*(n-1)/2)))
    
    
    for tt in range(0,48):
        print(month0[tt])
        covariance=pd.read_excel(path0+'covariance/cov-each-month/'+month0[tt]+'.xlsx').values
        siteaa= [int(x) for x in covariance[:,0]]
        covariance=np.delete(covariance, 0,axis=1)
        
        for k in range(n_group):
            site_sel=site[k]
            n0=len(site[k])
            count=0
            for i in range(n0):
                if site_sel[i] in siteaa:
                   indi=siteaa.index(site_sel[i])
                   for j in range(i):
                       if site_sel[j] in siteaa:
                          indj=siteaa.index(site_sel[j])
                          cor_all[k].cov[tt,count]=covariance[indi][indj]
                          cor_all[k].col[count]=(str(site_sel[i])+'-'+str(site_sel[j]))
                          count=count+1
                       else:
                           cor_all[k].cov[tt,count]=0
                           cor_all[k].col[count]=(str(site_sel[i])+'-'+str(site_sel[j]))
                           count=count+1
                else:
                    for j in range(i):
                        cor_all[k].cov[tt,count]=0
                        cor_all[k].col[count]=(str(site_sel[i])+'-'+str(site_sel[j]))
                        count=count+1
                    
                
        
        
    for k in range(n_group):
        df=pd.DataFrame(cor_all[k].cov)
        df.columns=cor_all[k].col
        df.to_excel(folder_path+cor_all[k].name+'_cov_hilbert.xlsx', index=False)
    
    
    
if __name__ == "__main__":
    get_pair_cov([alpha,beta,gamma,lammbda,delta,omicron], ['alpha','beta','gamma','lammbda','delta','omicron'])
    #get_pair_cov([omicron], ['omicron'])
