import socket

#start_client function -> allow a client to connect with a server
def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            #message var -> get a message from the user
            message = input("Enter a message to send to the server: ")
            #send the message and encode it
            s.sendall(message.encode())
            #condition if the user input it 'quit' end connection between client and server
            if message == 'quit':
                break
            #variable to store data
            data = s.recv(1024)
            #print back and decode
            print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()