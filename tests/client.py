"""
    Client Test Script
    Date: July 2021
"""

from uMQ import uMQ_Socket
import json

def process():

    print ("Creating a test JSON package to transmit to server.")

    data = {"Sample Data": "DEADBEEF", "Sample Data 2": "Test"}

    uMQIntance = uMQ_Socket()
    uMQIntance.connect("localhost", 5008)
    print ("Connected to Server.")
    uMQIntance.send_all (json.dumps(data))
    print ("Data Transmitted ... ")
    

if __name__ == "__main__":
    process()
