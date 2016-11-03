import socket
import sys

if __name__ == '__main__':
    if(len(sys.argv)< 4):
        print("Incorrect Params\nUsage: client.py <host> <port> <message>")
        exit()
        
    # create a TCP socket, connect on port 8000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((sys.argv[1], int(sys.argv[2])))
    
    clientSocket.send("GET /echo.php/?message=" + sys.argv[3] + " HTTP/1.0\r\n\r\n" )
    status = clientSocket.recv(10000)
    if(not status.startswith( "HTTP/1.0 200 OK")):
        print(status)
    message = clientSocket.recv(10000)
    print(message)
    