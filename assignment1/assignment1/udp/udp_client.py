from func_timeout import func_timeout
import socket, sys, time
#from timeout import timeout

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def connectUDP():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendToServer(s = None):
    waitingTime = 1
    if not s:
        s = connectUDP()
    server_ack = True
    print('Connected to the server.')
    print('Starting a file (upload.txt) upload...')
    with open("upload.txt","r") as file:
        curline = file.readline()
        reconnectTimes = [curline, 0]
        while curline:
            if reconnectTimes[0] != curline:
                reconnectTimes = [curline,0]
#            print("Send", str(curline).encode(),"to server")
            s.sendto(str(curline).encode(), (UDP_IP, UDP_PORT))
            try:
                data, ip = func_timeout(waitingTime, s.recvfrom, (BUFFER_SIZE,))
                print(f'Received ack({data.decode()}) from the server.')
                curline = file.readline() # if send succesful, then read the next line
            except:
                print("Package loss, resend it")
                reconnectTimes[1] +=1
                if reconnectTimes[1] < 3:    #reconnect less than 3 times
                    s = connectUDP()
                else:
                    print("sent it 3 times and fail")
                    exit()
        print("File upload successfully completed.")
        finishFlag = 'File upload successfully completed.'
        s.sendto(finishFlag.encode(), (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    sendToServer()
