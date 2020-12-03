import os, shutil

#for ens in range(14,20+1):
#for ens in range(15,20+1):
for ens in [14]:
    srcpath = '/home/utsumi/mnt/lab_tank/utsumi/WS/d4PDF_GCM/XX-HPB-%03d'%(ens)
    distdir = '/tank/utsumi/WS/d4PDF_GCM/'
    shutil.move(srcpath, distdir)
    print srcpath
    print distdir

