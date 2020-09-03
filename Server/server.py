################################
### Virtual Trading - SERVER  ##
### CREATED BY DAVID GOLDING ###
########### VERSION 5 ##########
################################


# Modules required for operation

import socket  # socket allows for networking
import threading  # threading allows for more than one line of code to be run at a given point
import mysql.connector  # mysql.connector allows for interaction with a mysql database
import commands  # commands allows for the manipulation of data within a database
import datetime  # datetimeallows for python to determine the current time
import urllib.request  # urllib.request allows for the interaction with webpages
import json  # json allows for python to understand the contents of json files
import ssl  # ssl allows for urllib.request to access webpages that are secure

# Classes


# Class 'Database' gives the server program the ability to interact with the database, using mysql.connector. Database
# uses the instance method, rather than a class method, meaning that all variables defined within the class method
# are encapsulated, and can only be accessed where an instance has been created. It is possible to think as a class
# method as creating a global variable, where as an instance method is creating a local variable.


class Database:

    def __init__(self):
        self.myDB = mysql.connector.connect(host="mysql6.gear.host", port=3306,
                                            user="csnea1", passwd="Je501b!k33C~",
                                            db="csnea1")
        # This creates the physical connection between the program
        # and the mysql database, assigning this connection to the
        # variable named myDB. The command mysql.connector.connect
        # contains all the arguments required for its operation.
        # This is the primary reason for the Server-Client setup
        # because it means that the user is given no information
        # to allow them physical access to the database, which would
        # compromise other users information.

        self.cursor = self.myDB.cursor(buffered=True)
        # This defines the cursor, which is used to retrieve data
        # from the database via sql commands

# Class 'Listen' gives the server program the ability to create new connections, and send and recieve data. Here the instance
# method is used, so that when a new user connects, a new instance is created which can't interact with previous ones.


class Listen:

    def connection(self, c, addr):  # The connection method gives the server program the instructions for when the user
                                    # sends data.
        access_database = Database() # An instance of the database class is created within Listen, in order to allow for the manipulation of data within it
        while True:    # A loop for two reasons. One is because it is not known when a user is going to send data, so
                       # therefore the program must continuously check. The other reason is that it is not known the volume
                       # of request that a given client is going to make.
            try:    # Try and except required to catch any errors that could occur with the client quiting their program,
                    # allowing for the program not to finish due to an error
                action = c.recv(1024).decode()     # The variable self.action is assigned to the contents of the received
                                                        # data
                if action != '':
                    action = eval(action) # The contents of self.action is the evaluated (containing the command
                                                    # to be carried out, as well as any data needed to complete this). This
                                                    # converts the list, which was stored as an array, back into a list which
                                                    # is capable of being manipulated.
                    while True:  # A while loop here is used to catch any errors that may be caused
                        try:
                            response = eval('commands.'+action[0]+'('+str(action)+', access_database)')
                            # The variable self.response forms the command needed in order to carry out the users request.
                            # This is then executed due to the eval statement, with any data that needs to be sent back
                            # being held in the self.response argument.
                            break  # Loop then breaks to allow the server to return the data to the client
                        except mysql.connector.errors.InterfaceError or mysql.connector.errors.OperationalError:
                        # Any error caused due to the database is caught,and the program will one again try to execute the
                        # command required.
                            pass

                    if isinstance(response,list) == True:  # isinstance is able to determine the data type a variable is.
                                                                # Here it has been used to determine whether self.response
                                                                # is a list. If this is true, then this means that self.response
                                                                # is graph data, and this has a special method to return
                                                                # packets to the client, as the entire list would exceed
                                                                # the maximum allowed packet size. Therefore it has been
                                                                # split, into manageable sizes in a list, that can be sent
                                                                # individually, and reassembled on the client side.
                        for values in response:    # Here it iterates through the items in the list, and for each items
                                                        # it sends it.
                            c.send(values.encode())
                    else:   # If the data is not a list, and a single packet is sent, as any data will not exceed the maximum
                            # packet side.
                        c.send(response.encode())

            except ConnectionAbortedError or ConnectionResetError:  # Once again any error is caught, and the server
                                                                    # will retry.
                pass

    def __init__(self, s):
        while True:     # This is looped to allow for the program to accept more than one connection at a given point.
                        # without this, the server would only be able to serve data to one client and any other clients
                        # requiring data would not able to retrieve it
            c, addr = s.accept()  # New connections are accepted, with self.c containing the socket data,
                                            # including the return address, of the client, where as self.addr contains
                                            # soley the return address
            t = threading.Thread(target=self.connection, args=(c, addr)) # Threading is used here to
                                                                                        # allow for the server program to
                                                                                        # execute different users requests
                                                                                        # simultaneously. Without using
                                                                                        # threading, a user would have to
                                                                                        # wait in a queue until all requests
                                                                                        # from other clients had been
                                                                                        # carried out. Therefore, each
                                                                                        # time a new client connects, a
                                                                                        # new thread of self.connection
                                                                                        # is created, with the arguments
                                                                                        # containing the clients information.
            t.start()  # Starts the thread


# Class 'Server' gives the program the ability to utilise the classes above. As well as this, it allows for the retrieval
# of the latest Forex data


class Server:

    def update(self):
            access_database = Database() # An instance of the database class is created within update, in order to allow for the manipulation of data within it
            updatetime = datetime.datetime.now()    # Determines the current time using the imported library datetime
            context = ssl._create_unverified_context()  # Allows for webpages which aren't secure to be opened
            while True:  # Loops, so while the server is running it is constantly in an update cycle
                try:
                    if datetime.datetime.now() > updatetime:  # If the current time is before the open time
                        with urllib.request.urlopen("https://forex.1forge.com/1.0.2/quotes?pairs=AUDCAD,AUDCHF,AUDEUR,AUDGBP,AUDJPY,AUDNOK,AUDNZD,AUDSEK,AUDTRY,AUDUSD,AUDZAR,CADAUD,CADCHF,CADEUR,CADGBP,CADJPY,CADNOK,CADNZD,CADSEK,CADTRY,CADUSD,CADZAR,CHFAUD,CHFCAD,CHFEUR,CHFGBP,CHFJPY,CHFNOK,CHFNZD,CHFSEK,CHFTRY,CHFUSD,CHFZAR,EURAUD,EURCAD,EURCHF,EURGBP,EURJPY,EURNOK,EURNZD,EURSEK,EURTRY,EURUSD,EURZAR,GBPAUD,GBPCAD,GBPCHF,GBPEUR,GBPJPY,GBPNOK,GBPNZD,GBPSEK,GBPTRY,GBPUSD,GBPZAR,JPYAUD,JPYCAD,JPYCHF,JPYEUR,JPYGBP,JPYNOK,JPYNZD,JPYSEK,JPYTRY,JPYUSD,JPYZAR,NOKAUD,NOKCAD,NOKCHF,NOKEUR,NOKGBP,NOKJPY,NOKNZD,NOKSEK,NOKTRY,NOKUSD,NOKZAR,NZDAUD,NZDCAD,NZDCHF,NZDEUR,NZDGBP,NZDJPY,NZDNOK,NZDSEK,NZDTRY,NZDUSD,NZDZAR,SEKAUD,SEKCAD,SEKCHF,SEKEUR,SEKGBP,SEKJPY,SEKNOK,SEKNZD,SEKTRY,SEKUSD,SEKZAR,TRYAUD,TRYCAD,TRYCHF,TRYEUR,TRYGBP,TRYJPY,TRYNOK,TRYNZD,TRYSEK,TRYUSD,TRYZAR,USDAUD,USDCAD,USDCHF,USDEUR,USDGBP,USDJPY,USDNOK,USDNZD,USDSEK,USDTRY,USDZAR,ZARAUD,ZARCAD,ZARCHF,ZAREUR,ZARGBP,ZARJPY,ZARNOK,ZARNZD,ZARSEK,ZARTRY,ZARUSD&api_key=TFcB6ULGXrCO28IF9lAyskzFTVtyWsci", context=context) as url:
                            # New data is requested from the data source
                            data = json.loads(url.read().decode())  # The data is then read using the json module
                                                                    # (due to the data source providing data in a json
                                                                    # format)
                        time = str(datetime.datetime.fromtimestamp(data[0]['timestamp']).strftime('%Y%m%d%H%M%S'))

                        # The update time contained within the json file is the stored in the variable 'time'
                        sqlstringa = "INSERT INTO data (date, "     # sqlstringa and sqlstringb are constructors
                                                                            # for an sql command
                        sqlstringb = "VALUES ('"+time+"', "
                        for i in data:  # For each symbol contained within the json file, it is appended to the string
                                        # with its associated price being stored in sqlstringb
                            sqlstringa += str(i["symbol"]) + ', '
                            sqlstringb += "'"+str(i["price"])+"', "
                        access_database.cursor.execute(sqlstringa[:-2]+') '+sqlstringb[:-2]+')')  # The sqlstringa and sqlstringb
                                                                                           # are combined and executed
                        access_database.myDB.commit() # The data added to the database is the committed
                        updatetime = datetime.datetime.now() + datetime.timedelta(minutes=20)   # The update time is then
                                                                                                # incremented by 20 minutes
                except mysql.connector.errors.OperationalError:  # Catches any error that may be caused by updating the database
                    pass
    def __init__(self):
        self.x = threading.Thread(target=self.update)   # Threading is used here in order to allow for the Forex data to be
                                                        # update simultaneously with the execution of commands for the client
        self.x.start()  # The thread is then started



        self.host = '0.0.0.0' # self.host specifies the host ip
        self.port = 2222  # self.host specifies the host port
        self.s = socket.socket()  # A socket is created
        self.s.bind((self.host, self.port))  # The host and port are bound to the socket
        self.s.listen(10)  # Allows for new connections with clients
        Listen(self.s)  # Creates the 'Listen' class, to allow for interaction with clients

if __name__ == '__main__':  # This determines if the server.py file is being run directly, or being imported through
                            # another file.
    Server()    # If it is being run directly, then the 'Server' class is created
