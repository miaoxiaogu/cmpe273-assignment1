import socket,sys
from threading import Thread


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(10)

    print(f"Server started at port {TCP_PORT}")

    while True:
        conn,addr = s.accept()
#        data = conn.recv(BUFFER_SIZE)
#
        try:
            sc_client = Thread(target = tcp_server, args = (conn,addr))
            sc_client.start()
        except KeyboardInterrupt:
            return


def tcp_server(conn, addr):
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print('No data received.')
                break
            print(f"Received data:{data.decode()}")
            conn.send("pong".encode())



if __name__ == "__main__":
    listen_forever()


