# import serial
# import time
#
# from serial.tools import list_ports
# port = list(list_ports.comports())
# for p in port:
#     print(p.device)
#
# baudrate = 9600
# port = '/dev/cu.usbserial-B002LEX7'
#
# #serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
# serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1)
# serialString = ""
# message=""
#
# def send(dealerInfo, player1Info, player2Info, player3Info, trueCount):
#     while True:
#         try:
#             inStrin = input("Press Enter to Send: ")
#             message = dealerInfo + ',' + player1Info + ',' + player2Info + ',' + player3Info + ',' + trueCount
#             #lengthpref = f"{len(message):03d}"
#             serialPort.write((message).encode())
#             print("Just Sent")
#             time.sleep(1)
#             serialString = serialPort.readline()
#             print("RECEIVED: ", serialString)
#             time.sleep(1)
#         except KeyboardInterrupt:
#             break
#
# serialPort.close()


import serial
import time

from serial.tools import list_ports
port = list(list_ports.comports())
for p in port:
    print(p.device)

def send(dealerInfo, player1Info, player2Info, player3Info, trueCount):
    baudrate = 9600
    port = '/dev/cu.usbserial-B002LEX7'

    #serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
    serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1)
    serialString = ""
    message=""

    while True:
        try:
            inStrin = input("Press Enter to Send: ")
            #message = inStrin
            message =  dealerInfo + ',' + player1Info + ',' + player2Info + ',' + player3Info + ',' + trueCount
            #lengthpref = f"{len(message):03d}"
            serialPort.write((message).encode())
            print("Just Sent")
            time.sleep(1)
            serialString = serialPort.readline()
            print("RECEIVED: ", serialString)
            time.sleep(1)
        except KeyboardInterrupt:
            break
    serialPort.close()

