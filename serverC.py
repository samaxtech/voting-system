# Server C

import socket
import time
import threading
import numpy
import pickle

# Declaring ips and ports
A_ip = '127.0.0.1'
A_port = 10011

B_ip = '127.0.0.1'
B_port = 20022

C_ip = '127.0.0.1'
C_port = 30033



def update(C_socket_speaks,local_2dtt,local_log):
    threading.Timer(0.5,update,args=(C_socket_speaks,local_2dtt,local_log,)).start()
    if networkWorks==True:
        table_sent=numpy.array([local_2dtt[1][0],local_2dtt[1][1],local_2dtt[1][2],local_2dtt[2][0],local_2dtt[2][1],local_2dtt[2][2]])
        #table_sent_str=str(table_sent)
        #str_log=pickle.dumps(local_log)
        table_sent_str=str(table_sent[0])+str(table_sent[1])+str(table_sent[2])+str(table_sent[3])+str(table_sent[4])+str(table_sent[5])
        
        # Log send
        log_array = pass_log(local_log)
        for i in log_array:
            table_sent_str += str(i)
        
        #print('\n',table_sent_str,'\n')
        C_socket_speaks.send(table_sent_str.encode())
        print('\nMessage sent from Server C to A')

        with open('state_severC.p', 'wb') as pfile:
            pickle.dump(local_dict, pfile)
            pickle.dump(local_log, pfile)
            pickle.dump(local_2dtt, pfile)


    
def update_table_C(array,local_2dtt):
    #threading.Timer(3.0,update_table_C,args=(array,local_2dtt,)).start()
    #print('Array to update Table C')
    #print(array)
    a=local_2dtt[0][0]
    b=local_2dtt[0][1]
    c=local_2dtt[0][2]
    d=local_2dtt[1][0]
    e=local_2dtt[1][1]
    f=local_2dtt[1][2]
    
    local_2dtt[0][0]=max(array[0],a)
    local_2dtt[0][1]=max(array[1],b)
    local_2dtt[0][2]=max(array[2],c)
    local_2dtt[1][0]=max(array[3],d)
    local_2dtt[1][1]=max(array[4],e)
    local_2dtt[1][2]=max(array[5],f)
    
    local_2dtt[2][0]=max(max(local_2dtt[0][0],local_2dtt[1][0]),local_2dtt[2][0])
    local_2dtt[2][1]=max(max(local_2dtt[0][1],local_2dtt[1][1]),local_2dtt[2][1])
    local_2dtt[2][2]=max(max(local_2dtt[0][2],local_2dtt[1][2]),local_2dtt[2][2])
    
    #printTable()
    
def update_log(array,local_log,local_2dtt):
    length_array = len(array)
    length_log = len(local_log['data'])
    if length_array < 6 or length_array < length_log+6:
        return
    supposed_length_log = sum(local_2dtt[1][:])
    if supposed_length_log > length_log:
        logs2add = supposed_length_log-length_log
    else:
        return
    i=1
    a=0
    start = 6+length_log
    while i:
        #print('First a\n',start,'\n')
        start = start+a
        if array[start]==0:
            local_dict['A']+=1
            new_log={}
            new_log['Vote']='A'
            add_log(new_log)
        elif array[start]==1:
            local_dict['B']+=1
            new_log={}
            new_log['Vote']='B'
            add_log(new_log)
        a+=1
        #print('Second a\n',start,'\n')
        if a>=logs2add:
            i=0
    
def update_receive(connC,local_2dtt,local_log):
    threading.Timer(0.5,update_receive,args=(connC,local_2dtt,local_log,)).start()
    time.sleep(2)
    #data = pickle.loads(connC.recv(512))
    data=connC.recv(512).decode()
    length_data=len(data)
    i=1
    a=0
    array_2dtt=[]
    while i:
        array_2dtt.append(int(data[a]))
        a+=1
        if a>=length_data:
            i=0
        
    if array_2dtt:
        print('Message received from Server B\n')
    '''
    #if not data:
        #break
    print (data,"\n")
    '''
    #print('\nRECEIVED\n',array_2dtt,'\n')
    update_log(array_2dtt,local_log,local_2dtt)
    update_table_C(array_2dtt,local_2dtt)
    garbageCollection(local_2dtt)
        
def garbageCollection(local_2dtt):
    if local_2dtt[0][2] == local_2dtt[1][2] and local_2dtt[1][2] == local_2dtt[2][2]:
        local_log={'data':[]}

def add_log(new_log):
	local_log['data'].append(new_log)

def voteA():
    local_dict['A']+=1
    new_log={}
    new_log['Vote']='A'
    add_log(new_log)
    local_2dtt[2][2]+=1

def voteB():
    local_dict['B']+=1
    new_log={}
    new_log['Vote']='B'
    add_log(new_log)
    local_2dtt[2][2]+=1
    
def pass_log(local_log):
    array = []
    for i in local_log['data']:
        if i == {'Vote': 'A'}:
            array.append(0)
        elif i == {'Vote': 'B'}:
            array.append(1)
    return array
'''    
def delete_log(local_log):
    local_log['data']=[]
'''	
def printDict():
    print(local_dict)
    
def printLog():
    print(local_log['data'])
    
def printTable():
    print (local_2dtt)

def command_response(command):
    if command=='Vote,A':
        voteA()
    elif command=='Vote,B':
        voteB()
    elif command=='printDict':
        printDict()
    elif command=='printLog':
        printLog()
    elif command=='printTable':
        printTable()

def Main():

    #Local Dictionary:
    n=0
    m=0
    global local_dict
    local_dict={'A':n,'B':m}

    #Local LOG:
    global local_log
    local_log={'data':[]}

    #Local 2DTT:
    global local_2dtt
    local_2dtt = numpy.array([[0,0,0],[0,0,0],[0,0,0]])

    #Network Failure Emulator:
    global networkWorks 
    networkWorks=True
    
    # Create sockets:
    # Speaking socket:
    C_socket_speaks = socket.socket()   #Destination socket: from server C to server A:
    C_socket_speaks.connect((A_ip,A_port))
    # Hearing socket:
    C_socket_hears = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #Listening socket (listens to server B).
    C_socket_hears.bind((C_ip,C_port))
    C_socket_hears.listen(1)
    print("\nServer C ready and listening...\n")
    connC, addr = C_socket_hears.accept()
    


    with open('state_severC.p', 'rb') as pfile:
        local_dict = pickle.load(pfile)
        local_log = pickle.load(pfile)
        local_2dtt = pickle.load(pfile)



    update(C_socket_speaks,local_2dtt,local_log)
    update_receive(connC,local_2dtt,local_log)
    
    while True:
        print "\n----------------------------------------\n"
        command=raw_input("ENTER COMMAND/ACTION FOR SERVER: \n----------------------------------------\n")


        if command=='networkFail':
            networkWorks=False
        elif command=='networkWorks':
            networkWorks=True
        command_response(command)
        
        
    C_socket_hears.close()


if __name__ == '__main__':
        Main()

