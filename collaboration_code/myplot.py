import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import sg_filter
import os
for myfile in os.listdir(os.curdir):
	if myfile.endswith(".txt"):
		print myfile
		data=np.loadtxt(myfile)
		X=data[:,0]
		Y1=data[:,1]
		Y2=data[:,2]
		Y1 = sg_filter.savitzky_golay(Y1, 111, 1)
		Y2 = sg_filter.savitzky_golay(Y2, 111, 1)
		plt.plot(X,Y1,label="Azure QoE")
		plt.plot(X,Y2,label="Google QoE")
		plt.legend(loc='upper left')
		plt.xlabel("Time")
                plt.title("Google Vs Azure QoE")
		#plt.show()
		filename=myfile.replace("txt","")
		plt.savefig(filename+'png')
		plt.close()
