__author__ = 'Maximilian_H'

import main
import time
import cryptographer as cr



import threading
import Queue

result_q = Queue.Queue()
data_q = Queue.Queue()
stop_q = Queue.Queue()

def worker(data_q, result_q, stop_q):
    while stop_q.get() != "STOP":
        data = data_q.get()
        data = data + 1
        result_q.put(data)

myThread = worker(data_q, result_q, stop_q)

data_q.put(1)
myThread.start()
i = 2
for l in range(20):
    print result_q
    if l == 20:
        stop_q.put("STOP")
        break
    data_q.put(i)



#main.Startup.startup()

#main.VarKeeper.s_key = main.Security.loadkey()
#print "SKey: "+str(main.VarKeeper.s_key)
#main.Security.loadthosts()
#print "THosts: "+str(main.VarKeeper.trusted_hosts)
#console = main.Multiprocessing.new(main.BG_Functions.input_system_console(), "Console")
#sock_remote_listener_dict = main.Multiprocessing.new(main.BG_Functions.socket_remote_access_listener(), "SocketRemoteAccessListener")

#main.Multiprocessing.start(console)
#main.Multiprocessing.join(console)