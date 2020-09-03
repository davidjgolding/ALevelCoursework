import socket  # This imports the socket module
import login
class Connect:
    def show_login(self):
        show = login.Show()
        show.get_credentials()
        show.verify_credentials()
    def __init__(self, host, port, s):
        self.host = host  # Specifies the address where the server can be accessed
        self.port = port  # Specifies the port number that the server will be listening to
        self.s = socket.socket()  # This creates the socket
        self.s.connect((host, port))  # This connects to the server

if __name__ == '__main__':
    start = Connect('0.0.0.0', 1115)
