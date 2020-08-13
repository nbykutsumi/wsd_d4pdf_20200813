# %%
import numpy as np
import pygrib
import matplotlib.pyplot as plt
#%matplotlib inline

#vname = 'BRTMPsfc'
#vname = 'surface Geopotential'
srcpath = '/home/utsumi/mnt/lab_data2/JRA55/Hist/Monthly/fcst_surf125/fcst_surf125.198010'
with pygrib.open(srcpath) as grbs:
    #print grbs.message(1)
    #print grbs.message(2)
    #print grbs.message(3)
    #print grbs.message(4)
    #print grbs.message(5)
    #print grbs.message(6)
    #print grbs.message(7)
    #print grbs.message(8)
    for grb in grbs:
        print grb
    #grb = grbs.select(shortName=vname)[0]
    #grb = grbs.select(name=vname)[0]
#aout = np.flipud(grb.values)
#print aout
#plt.imshow(aout, origin='lower')
#plt.colorbar()
#plt.title(vname)
#plt.show()   


# %%
