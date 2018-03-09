#
# Semaphore.py
# CS3070 
#
# created: Spring '16
# updated: Summer '17
#

'''This is the Semaphore implementaion class.'''
class Semaphore(object):


##########################################
#Constructor


    def __init__(self, n, simKernel):
        ''' use as provided.
            - n is the number to set the Semaphore counter to initially
            - simKernel provides the access to the simulated kernel a real OS
                 would have when constructing a Semaphore'''
        
        self.OS = simKernel
        
        #self.counter = n
        #self.queue = []
        #self.lock = lock 
                
        #TODO: implement the rest of the constructor as required
        #self.OS.write(n,counter)




##########################################
#Instance Methods



    def wait(self, caller):
        ''' semaphore wait functionality.
            - caller is the process asking "wait?"
              (you will need caller because this is a simulated system,
               a production OS has this info available as part of the PCB)'''
        #TODO: implement 
        '''WAIT(s):
            with s.lock:
                s.c--
                if s.c<0 then
                    SAVESW
                    attach(PID, s.q)
                    set PID = detach(RL)
                    LOADSW
            return
        '''
 

    def signal(self, caller):
        ''' semaphore signal functionality.
            - caller is the process providing the "signal"
              (you will need caller because this is a simulated system,
               a production OS has this info available as part of the PCB)'''
        #TODO: implement 
        '''SIGNAL(s):
            with s.lock:
                s.c++
                if s.c<=0 then
                    P = detach(s.q)
                    attach(P, RL)
                return'''
            