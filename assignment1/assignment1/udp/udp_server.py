import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print(f"Server started at port {UDP_PORT}.")
    print("Accepting a file upload...")

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        #print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
        if data.decode() == "File upload successfully completed.":
           print("Upload successfully completed.")
        else:
            ack = data.decode().split(":")[0]
            # reply back to the client
            s.sendto((ack).encode(), ip)


if __name__ == "__main__":
    listen_forever()
