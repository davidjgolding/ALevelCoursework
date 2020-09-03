import socket
import mysql.connector
import threading

class Database:
    def execute(self, command):
        connection.cursor.execute(command)  # SQL which selects all data
        data = connection.cursor.fetchall()  # The response is extracted from the cursor
        return data
    def __init__(self):
        self.myDB = mysql.connector.connect(host="mysql6.gear.host", port=3306,
                                            user="csnea1", passwd="Je501b!k33C~",
                                            db="csnea1")
        self.cursor = self.myDB.cursor(buffered=True)

connection = Database()  # This creates an instance of database
data = connection.execute("SELECT * FROM tbl_users;")
print (data)
class NewConnection:
    def requests(self):  # The connection method gives the server program the instructions for when the user
                                    # sends data.
        while True:    # A loop for two reasons. One is because it is not known when a user is going to send data, so
                       # therefore the program must continuously check. The other reason is that it is not known the volume
                action = eval(self.c.recv(1024).decode())     # The variable self.action is assigned to the contents of the received
                                                        # data. The contents of self.action is the evaluated (containing the command
                                                    # to be carried out, as well as any data needed to complete this). This
                                                    # converts the list, which was stored as an array, back into a list which
                                                    # is capable of being manipulated.
                response = eval('commands.'+action[0]+'('+str(action)+', self.access_database)')
                            # The variable response forms the command needed in order to carry out the users request.
                            # This is then executed due to the eval statement, with any data that needs to be sent back
                            # being held in the self.response argument.
                self.c.send(response.encode())

    def __init__(self, c, addr, access_database):
        self.c = c
        self.addr = addr
        self.access_database = access_database

class Server:
    def new_client(self, c, addr, access_database):
        instance = NewConnection(c, addr, access_database)
        instance.requests()
    def allow_access(self):
        access_database = Database()
        while True:
            c, addr = self.s.accept()
            t = threading.Thread(target=self.new_client, args=(c, addr, access_database))
            t.start()
    def __init__(self, host, port, connections):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(connections)

if __name__ == '__main__':
    start = Server('0.0.0.0', 1115, 100)
    start.allow_access()


def new_client(self):
    # Allows for a new connection by a client
    data = eval(self.c.recv(1024).decode()) # Waits to receive data from the
                                       # client. The data from client can be a
                                       # maximum of 1024 bits. Once the data is
                                       # received, it is evaluated to convert
                                       # the data from a string to a list
    email = data[0]  # Data is indexed and the variable email stores the first item
                     # in data
    password = data[1]  # Data is indexed and the variable password stores the
                        # second item in data
    print("User's email is: " + email + ", and their password is: " + password +
          ".")
    # A string is created containing both items of data and printed
    response = "Welcome!"  # The variable response holds a string
    self.c.send(response.encode())  # The string is encoded and sent to the client


def login(self): #
    email = input('Email: ')  # User inputs their email
    password = input('Password: ') #  User inputs their password
    data = str([email, password])  # email and password are inserted into a
                                  # list, which is converted to a string and
                                  # stored as data
    self.s.send((data.encode()))  # data is encoded and sent to Server
    response = self.s.recv(1024).decode()  # Client waits for a response from
                                          # server, decodes it and stores it in
                                          # response
    print(str(response))  # response is converted to a string and printed


import socket  # This imports the socket module
import threading  # This imports the threading module

class Server:
    def receive_login(self):
        data = eval(self.c.recv(1024).decode())
        email = data[0]
        password = data[1]
        print("User's email is: " + email + ", and their password is: " + password +
              ".")
        response = "Welcome!"
        self.c.send(response.encode())
    def new_client(self):
        while True:
            c, addr = self.s.accept()
            t = threading.Thread(target=self.receive_login, args=(c, addr))
            t.start()
    def __init__(self, host, port, connections):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        self.s.listen(connections)
        self.c, self.addr = self.s.accept()
if __name__ == '__main__':
    start = Server('0.0.0.0', 1111, 1)