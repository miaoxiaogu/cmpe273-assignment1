import socket,sys,time
#
#
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(id):
    delayInSec = int(sys.argv[2])
    numOfPingMessage = int(sys.argv[3])
    num = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while num < numOfPingMessage:
        s.send(f"{id}:{MESSAGE}".encode())
        print(f"Sending data:{MESSAGE}")
        data = s.recv(BUFFER_SIZE)
        print("Received data:", data.decode())
        num += 1
        time.sleep(delayInSec)
    s.close()

#
#
def get_client_id():
    id = sys.argv[1]
    return id

if __name__== "__main__":
    send(get_client_id())
