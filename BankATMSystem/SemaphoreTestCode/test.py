#
# test.py
# CS3070 
#
# created: Spring '16
# updated: Summer '17
#

from multiprocessing import Pipe   

from SL_Kernel import *
from Semaphore import *
from SimpleUser import *





if __name__ == '__main__':

    #sim OS initial boot
    OS = SL_Kernel()
    
    #set account name and initial value
    OS.write('test', 2000)


    #your Semaphore will be called here
    s = Semaphore(1, OS)


    #set up users and threads
    randomSeed = 42
    iterations = 20
    program1 = SimpleUser('P1', randomSeed,   'test', iterations, s, OS)
    program2 = SimpleUser('P2', randomSeed+1, 'test', iterations, s, OS)
    program3 = SimpleUser('P3', randomSeed+2, 'test', iterations, s, OS)
    
    #finish OS registration of the ATMServers program's Processes
    P1 = OS.getNewProcessOnSharedHardware( program1 )
    P2 = OS.getNewProcessOnSharedHardware( program2 )
    P3 = OS.getNewProcessOnSharedHardware( program3 )

    #boot up
    P1.start()
    P2.start()
    P3.start()

    
    #clean shutdown
    P1.join()
    P2.join()
    P3.join()


    final =  OS.read('test')
    print('Final total is', final)
    
    print('Done with test!')

