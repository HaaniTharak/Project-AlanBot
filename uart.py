import serial
import time

from serial.tools import list_ports
port = list(list_ports.comports())
for p in port:
    print(p.device)

def send(trueCount, player1Info, dealerInfo):
    if player1Info < 10:
        player1Info = '0' + str(player1Info)
    else:
        player1Info = str(player1Info)

    if trueCount < 10 and trueCount >= 0:
        trueCount = '0'+ '0' + str(trueCount)
    elif trueCount > 0:
        trueCount = '0' + str(trueCount)
    elif trueCount < 0 and trueCount > -10:
        trueCount = '1'+ '0' + str(abs(trueCount))
    else:
        trueCount = '1' + str(abs(trueCount))


    baudrate = 9600
    port = '/dev/cu.usbserial-B002LEX7'

    #serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
    serialPort = serial.Serial(port=port, baudrate=baudrate,bytesize=8, timeout=1)
    serialString = ""
    message=""

    # while True:
    #     try:
    #         inStrin = input("Press Enter to Send: ")    
    message = trueCount + player1Info + str(dealerInfo) + "\r"
    #print(message)
    #lengthpref = f"{len(message):03d}"
    while (serialString) != message:
        serialPort.write((message).encode())
        time.sleep(.75)
        print("Just Sent:", message)
        serialString = serialPort.readline()
        serialString = serialString.decode('ascii') + "\r"
        print("RECEIVED: ", serialString)
    
    return