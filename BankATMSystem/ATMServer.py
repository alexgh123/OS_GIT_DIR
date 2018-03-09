#
# ATMServer.py
# CS3070 
#
# created: Spring '16
# updated: Winter '17
#


import random

from ATMMessage import *
from SL_Kernel import *


'''This is bank's ATM server class.
There are multiples of these running at the bank which may access the same accounts at the same time. It
does not matter if we think of them running on the same huge machine or many little ones, the data is shared.

It does not matter if the data is shared inside a database, a data structure, in a Non Uniform Memory Access
RAM, or in a sandard RAM.  Shared is shared and essentially the only thing that changes is timing.
'''
class ATMServer(object):


##########################################
#Constructor

    def __init__(self, cName, seed, account, transactionLimit, connectionOut, unused, kernel):
        
        #hardware initialization
        self.OS = kernel
        self.OS.read(account)   #verify we are connected to proper memory

        self.serverConection = connectionOut
        self.name = cName
        self.account = account

        
        self.__TRANSACTION_LIMIT__ = transactionLimit
        
        self.again = True
        random.seed(seed)
        
        #self.semaphore = Semaphore(lock, queue, counter)
        
##########################################
#Instance Methods


    def execute(self):
        '''this is the function passed to SL_Kernel.getNewProcessOnSharedHardware
           which serves as the processes "Run loop" '''

        i = 0
        while self.again:

            #check and act on sim's stop condition 
            if i >= self.__TRANSACTION_LIMIT__:
                self.again = False
                break

            i += 1
            
            #waiting for next message
            message = self.serverConection.recv()
            (operation, amount) = ATMMessage.unwrap(message)

            ##SEMAPHORE WAIT HERE  semaphore.wait(self)
            if operation == PUT_BALANCE:
                self.OS.write(self.account, amount)
                
            elif operation == GET_BALANCE:
                amount = self.OS.read(self.account)
                msg = ATMMessage.wrap(BALANCE, amount)
                self.serverConection.send(msg)
        
            else:
                raise RuntimeError(operation + 'is an unrecognized account operation')                    

            ##SEMAPHORE SIGNAL HERE semaphore.signal(self)
            
        
        self.serverConection.send(SHUTDOWN)
        print('   ATMServer', self.name, 'shut down')



    def setProcessReference(self, st):
        ''' having this is a requirement of SL_Kernel for any program process'''
        self.processReference = st



