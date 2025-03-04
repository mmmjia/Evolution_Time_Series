# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:29:50 2025

@author: user
"""
import pandas as pd
import numpy as np
import sys
import os

path0='C:/Users/user/OneDrive - HKUST Connect/cleanproteindata/'
folder_path = 'C:/Users/user/OneDrive - HKUST Connect/hilbert/cov_hilbert/'



year = ['2020','2021','2022','2023']; months = [str(i).zfill(2) for i in range(1,12+1)]
month0 = [i+'-'+j for i in year for j in months]
m=500
for tt in range(35,49):
    covariance=pd.read_excel(path0+'covariance/cov-each-month/'+month0[tt]+'.xlsx').values
    siteaa= [int(x) for x in covariance[:,0]]
    covariance=np.delete(covariance, 0,axis=1)
    covsele=np.triu(covariance)
    
    flattened_matrix = covsele.flatten()
    
    sorted_indices = np.argsort(flattened_matrix)[-m:]

    positions = np.unravel_index(sorted_indices, covsele.shape)
    
    variant_site1=[siteaa[int(site)] for site in positions[0]]
    variant_site2=[siteaa[int(site)] for site in positions[1]]
    
    
    cor_time=np.zeros((tt+1,500))

    for i in range(0,m):
                 
        cor_time[tt,i]=covariance[positions[0][i]][positions[1][i]]
    
    for mo in range(0,tt):
        covariance=pd.read_excel(path0+'covariance/cov-each-month/'+month0[mo]+'.xlsx').values
        siteaa= [int(x) for x in covariance[:,0]]
        covariance=np.delete(covariance, 0,axis=1)
        
        for i in range(0,m):
                if variant_site1[i] in siteaa:
                    indi=siteaa.index(variant_site1[i])                
                    if variant_site2[i] in siteaa:
                            indj=siteaa.index(variant_site2[i])                        
                            cor_time[mo,i]=covariance[indi][indj]
    
    df=pd.DataFrame(cor_time)
    col=[]
    for co in range(m):
        col.append(str(variant_site1[co])+'-'+str(variant_site2[co]))
    df.columns=col
    df.to_excel('C:/Users/user/OneDrive - HKUST Connect/hilbert/cov_hilbert/'+month0[tt]+'cov_hilbert.xlsx', index=False)
    print(month0[tt])

