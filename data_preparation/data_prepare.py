# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:47:13 2022

@author: MengQi
"""

import math
import pandas
import os
import tensorly as tl
import numpy as np
from tensorly.decomposition import tucker
from scipy.optimize import curve_fit
import pandas as pd
import re
import matplotlib
import openpyxl
import matplotlib.mlab as mlab
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import sys
from multiprocessing import Manager
from multiprocessing import Pool
from functools import partial
import numpy as np
import pandas as pd
from scipy.linalg import svdvals


path0='cleanproteindata/' ##put your sequence data here

P=np.zeros((30,45))
year = ['2020','2021','2022','2023']; months = [str(i).zfill(2) for i in range(1,12+1)]
month0 = [i+'-'+j for i in year for j in months]
strr=month0[0:38]
lenmonth=len(strr)
mutatedsite=np.zeros((1274,lenmonth))
mutation_total=np.zeros((lenmonth,21,1274))
for i in range(lenmonth):
    data_new=pd.read_excel(path0+strr[i]+'.xlsx', sheet_name=0).values
    data_new=np.delete(data_new,0,axis=1)
    mutation_total[i,:,:]=data_new
dataall=np.sum(mutation_total,axis=0)

aa = 'ACDEFGHIKLMNPQRSTVWY-'
aa2idx = {}
for i in range(len(aa)):   
    aa2idx[aa[i]] = i

data_orignal=pd.read_excel(path0+'orignal-site.xlsx', sheet_name=0)
data_orignal = data_orignal['Residues']
#print(data_orignal)
os.makedirs('C:\\olddata\\spyder-tensor\\mutation_aa_0203')
for i in range(1273):    
   si=data_orignal[i]
        #except:
         #   sys.stderr.write('can not create output directory: %s \n' % ('tensor-result2/result' + strr[month]) )
   sitereal=si[1:]
   mutationmonth_aa=mutation_total[:,:,int(sitereal)]
   plt.imshow(np.log(mutationmonth_aa+1), aspect='auto', cmap='Reds')
   xx = np.arange(0, 21)
   plt.title(sitereal)
   plt.xticks(xx, ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q',
                'R', 'S', 'T', 'V', 'W', 'Y', '-'])
   #plt.xlabel('a.a.')
   plt.colorbar()
   plt.savefig('C:/olddata/spyder-tensor/mutation_aa_0203'+ sitereal + '.png', dpi=300)
   plt.close()
#        plt.close()
        #plt.xlabel('a.a.')
   excelmutation=pd.DataFrame(mutationmonth_aa)
   excelmutation.to_excel('C:/olddata/spyder-tensor/mutation_aa_0203'+sitereal+'.xlsx') 

'''for q in range(16,21):
    os.makedirs('D:\\spyder-tensor\\mutation_aa\\mutation_aa' + str(q))
    for i in range(1273):    
        si=data_orignal[i]
        siaa=si[0]
        if siaa==aa[q]:       
            #except:
             #   sys.stderr.write('can not create output directory: %s \n' % ('tensor-result2/result' + strr[month]) )
            sitereal=si[1:]
            #print(sitereal)
            mutationmonth_aa=mutation_total[:,:,int(sitereal)]
            plt.imshow(np.log(mutationmonth_aa+1), aspect='auto', cmap='Reds')
            xx = np.arange(0, 21)
            plt.title(sitereal)
            plt.xticks(xx, ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q',
                    'R', 'S', 'T', 'V', 'W', 'Y', '-'])
            #plt.xlabel('a.a.')
            plt.colorbar()
            plt.savefig('D:/spyder-tensor/mutation_aa/mutation_aa' + str(q) +'/'+ sitereal + '.png', dpi=300)
            plt.close()
    #        plt.close()
            #plt.xlabel('a.a.')
            excelmutation=pd.DataFrame(mutationmonth_aa)
            excelmutation.to_excel('D:/spyder-tensor/mutation_aa/mutation_aa' + str(q)+'/'+sitereal+'.xlsx') '''
        


