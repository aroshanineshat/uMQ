"""
    Server Test Script
    Date: July 2021
"""

from uMQ import uMQ_Socket

def process():

    print ("Creating the uMQ server.")

    uMQIntance = uMQ_Socket()
    uMQIntance.server("localhost", 5008)
    while (True):
        uMQIntance.hold()
        print ("New Data Arrived.")
        while (uMQIntance.data_available()):
            data = uMQIntance.get_next_pkt()
            print (data) 
        uMQIntance.Clear()
        print ("Buffer printed, cleared the event flag and waiting for more data.")
        
        
        
if __name__ == "__main__":
    process()
