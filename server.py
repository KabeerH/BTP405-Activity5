import socket
import threading

#helper function handle_client_connection -> get connection from clients
def handle_client_connection(conn, addr):
    #address connected to display 
    print(f'Connected by {addr}')
    #While loop unti the user disconnects from server (enters 'quit' or keyboard force quit)
    while True:
        data = conn.recv(1024)
        if not data or data.decode() == 'quit':
            print(f'Connection closed by {addr}')
            break
        #print message to server
        print(f'Message recieved from client: {data.decode()}')
        #send the message
        conn.sendall(data)
    conn.close()

#start_server function -> starting and running the server
def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #bind the host and port
        s.bind((host, port))
        #display when server has started
        print(f'Server started, listening on {host}:{port}')
        #listen for connection
        s.listen()
        #While the server is up accept data and thread for multiple connections (call helper function)
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()