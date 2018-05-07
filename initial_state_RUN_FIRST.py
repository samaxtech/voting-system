import socket
import time
import threading
import numpy
import pickle



#Local Dictionary:
n=0
m=0
local_dict={'A':n,'B':m}

#Local LOG:
local_log={'data':[]}

#Local 2DTT:
local_2dtt = numpy.array([[0,0,0],[0,0,0],[0,0,0]])



with open('state_severA.p', 'wb') as pfile:
    pickle.dump(local_dict, pfile)
    pickle.dump(local_log, pfile)
    pickle.dump(local_2dtt, pfile)


with open('state_severB.p', 'wb') as pfile:
    pickle.dump(local_dict, pfile)
    pickle.dump(local_log, pfile)
    pickle.dump(local_2dtt, pfile)


with open('state_severC.p', 'wb') as pfile:
    pickle.dump(local_dict, pfile)
    pickle.dump(local_log, pfile)
    pickle.dump(local_2dtt, pfile)