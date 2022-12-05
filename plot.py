###########################
import emcee
import corner
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as pl
import subprocess
import sys
from os import listdir
from os.path import isfile, join
from scipy.integrate import quad
import random
import matplotlib.pyplot as plt
bin_num=11

input_f=np.genfromtxt('Initial.in')
rh=(input_f[:,0])
mass=(input_f[:,1])
rg=(input_f[:,2])

#######################################               PLOT------initial&&&&&&&&&&&&&&&&&&&&&&&&&&&&


#               PLOT


heights=2.0*9.5/2
widths=2.0*6.8/2.0

titlefntsize=28

xfntsize=21
yfntsize=21

xpad=2
ypad=1.4

ticfntsize=17

lgndfntsize=10
lgndloc=2

mew1=0
ms1=0
lw1=3



fig, ax1 = plt.subplots()                   
fig.set_size_inches(heights, widths)

#____________________________________________       Initial Mass

logm_I=np.log10(mass)

plt.hist(logm_I,bins=bin_num,range=[2, 7], histtype="stepfilled", edgecolor='b', facecolor='royalblue') 

plt.xlabel(r'$\mathregular{Log_{10}\ m_{i}\ [M_{\odot}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Initial_mass.eps')

plt.clf()



#____________________________________________       Initial Rg

logm_rg=np.log10(rg)

plt.hist(logm_rg,bins=bin_num,range=[-3, 2.2], histtype="stepfilled", edgecolor='b', facecolor='royalblue') 

plt.xlabel(r'$\mathregular{Log_{10}\ R_{G}\ [kpc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

 

plt.savefig('Initial_RG.eps')

plt.clf()



#____________________________________________       Initial rh



plt.hist(rh,bins=bin_num,range=[0, 35], histtype="stepfilled", edgecolor='b', facecolor='royalblue') 

plt.xlabel(r'$\mathregular{r_{h}\ [pc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Initial_rh.eps')

plt.clf()

###################################################################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&




####**********************************************************************FFFFFFFFFFFFFFFFFFfinal
####**********************************************************************FFFFFFFFFFFFFFFFFFfinal
input_f=np.genfromtxt('out.out')
rh_f=(input_f[:,1])
M_f=(input_f[:,2])
RG_f=(input_f[:,3])/1000.





###########################################################################################@@@@@@@@@@@@@@@@@@@@@@@


line_number=input_f.shape[0]/1.




logmass_f= np.log10(M_f)
logRG_f=np.log10(RG_f)


final_rh = np.histogram(rh_f, bins=bin_num, range=(0,35))
final_mass = np.histogram(logmass_f, bins=bin_num, range=(2,7))
final_logRG = np.histogram(logRG_f,  bins=bin_num, range=(-3,2.2))


rh_f_bins = np.column_stack(156* final_rh[0]/line_number)
logm_f_bins = np.column_stack( 156* final_mass[0]/line_number)
logRG_f_bins = np.column_stack( 156* final_logRG[0]/line_number)


Final_f=np.column_stack((rh_f_bins, logm_f_bins, logRG_f_bins))




###############################################################PLOT-------final@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#____________________________________________       Final Mass

logm_I=np.log10(M_f)
weights = [156.0/line_number] * len(logm_I)
#

entries, edges, _ = plt.hist(logm_I,bins=bin_num,weights=weights,range=[2, 7],histtype="stepfilled", edgecolor='b', facecolor='royalblue') 
expt_m=entries

plt.xlabel(r'$\mathregular{Log_{10}\ m_{i}\ [M_{\odot}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Final_mass.eps')

plt.clf()

#____________________________________________       Final Rg

logm_rg=np.log10(RG_f)

entries, edges, _ = plt.hist(logm_rg,bins=bin_num,weights=weights,range=[-3, 2.2], histtype="stepfilled", edgecolor='b', facecolor='royalblue') 
expt_rg=entries

plt.xlabel(r'$\mathregular{Log_{10}\ R_{G}\ [kpc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

 

plt.savefig('Final_RG.eps')

plt.clf()



#____________________________________________       Final_rh



entries, edges, _ = plt.hist(rh_f,bins=bin_num,weights=weights,range=[0, 35], histtype="stepfilled", edgecolor='b', facecolor='royalblue') 
expt_rh=entries

plt.xlabel(r'$\mathregular{r_{h}\ [pc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Final_rh.eps')

plt.clf()




####################################################HHHHHHHHHHOOOOOOOOOOOOOLLLLLLLLLLLGGGGGGERRRRRRRRRRRR


data0 = np.loadtxt("Holger-M-RG-rh-156-clusters.hol")


#____________________________________________       Initial Mass

logm_I=np.log10(data0[:,0])

entries, edges, _ = plt.hist(logm_I,bins=bin_num, range=[2, 7], histtype="stepfilled", edgecolor='g', facecolor='palegreen') 
bin_centers = 0.5 * (edges[:-1] + edges[1:])
plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')
#sigma_m = [1.0] * (bin_num)
sigma_m = np.sqrt(entries)
HB_m=entries

plt.xlabel(r'$\mathregular{Log_{10}\ m_{i}\ [M_{\odot}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Holger_mass.eps')

plt.clf()



#____________________________________________       Initial Rg

logm_rg=np.log10(data0[:,1])

entries, edges, _ = plt.hist(logm_rg,bins=bin_num,range=[-3, 2.2], histtype="stepfilled", edgecolor='g', facecolor='palegreen') 
bin_centers = 0.5 * (edges[:-1] + edges[1:])
plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')
#sigma_rg = [1.0] * (bin_num)
sigma_rg = np.sqrt(entries)
HB_rg=entries

plt.xlabel(r'$\mathregular{Log_{10}\ R_{G}\ [kpc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

 

plt.savefig('Holger_RG.eps')

plt.clf()



#____________________________________________       Initial rh

rh=data0[:,2]

entries, edges, _ = plt.hist(rh,bins=bin_num, range=[0, 35], histtype="stepfilled", edgecolor='g', facecolor='palegreen') 
bin_centers = 0.5 * (edges[:-1] + edges[1:])
plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')
#sigma_rh = [1.0] * (bin_num)
sigma_rh = np.sqrt(entries)
HB_rh=entries

plt.xlabel(r'$\mathregular{r_{h}\ [pc}]}$',fontsize = xfntsize, labelpad=xpad)
plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

plt.xticks(fontsize = ticfntsize)
plt.yticks(fontsize = ticfntsize)

plt.savefig('Holger_rh.eps')

plt.clf()





#################################################################################################










############################################################################ki2

