################################
## Virtual Trading - COMMANDS ##
### CREATED BY DAVID GOLDING ###
########### VERSION 5 ##########
################################


# Modules required for operation

import smtplib  # Allows for the creation of a SMTP client session to send emails
import codecs  # Allows for the opening of files, and the decoding of these files using a certain codec
from email.mime.text import MIMEText  # MIMEText (Multipurpose Internet Mail Extensions) allows for text to be encoded
                                      # in the MIME format
from email.mime.multipart import MIMEMultipart  # Allows for the sending of both an HTML and TEXT part of an email
                                                # message in a single email
import random  # Allows for a random integer to be generated

# The procedure and function below are required in multiple instances within the objects, and therefore, they don't
# have a parent

# The procedure send_email, allows for the sending of email to a user

def send_email(x,y,z):
    fromaddr = "dgcscoursework@gmail.com"  # The variable, fromaddr, specifies the email address that the email is
                                           # being sent from
    toaddr = x  # The variable, toaddr, specifies the address that the email is being sent to, and is passed through
                # when the procedure called with the parameter x
    msg = MIMEMultipart('alternative') # This tells the email client application how to properly display the content
    msg['From'] = 'Virtual Trading Team <dgcscoursework@gmail.com>'
    msg['To'] = x
    msg['Subject'] = y
    msg.attach(MIMEText(z, 'html')) # Here the parameter z, containing the content of the message, is attached to msg
                                    # with MIMEText encoding the text into base64, and specifying the content type as
                                    # html
    server = smtplib.SMTP('smtp.gmail.com', 587)  # A connection is created with the email server, Gmail, with its
                                                  # respective port
    server.starttls()  # This connection is then started
    server.login("dgcscoursework@gmail.com", "dgcscoursework!")  # The credentials (username, passsword) are then used
                                                                 # to log into the Gmail account
    text = msg.as_string() # The MIME message is converted to a string, so that it is ready to be sent
    server.sendmail(fromaddr, toaddr, text)  # The sendmail procedure is called, sending the contents of text, to the
                                             # email address held in toaddr
    server.quit()  # The connection is then terminated

# The function email_check, returns the tuple for a user, when given an email address

def email_check(y, z):
    z.cursor.execute("SELECT * FROM csusers WHERE Email='" + y + "'")  # Here the sql statement is executed using
                                                                       # Database, which has been passed in via the
                                                                       # parameter z. This sql statement requests that
                                                                       # all columns are returned where the email
                                                                       # address column is equal to the parameter y
    fetch = z.cursor.fetchall()  # The data is extracted from the cursor using the z.cursor.fetchall() command, with the
                                 # variable fetch holding that specific users data in a list form
    return fetch  # The data is then returned

# The object SignIn verifies a users credentials, making sure that the details entered on the client side match with
# data held within the database. The object uses the class method, instead of the instance method, so that it is able
# to return data to another object.

class SignIn:
    def check(y, z):  # The function check verifies whether the username and password entered, contained in parameter y,
                      # is equal to the data stored within the database
        fetch = email_check(y[1],z)  # The function email_check is used to return the data relating to the user which
                                     # has the email address, matching the one entered by the user, stored as y[1]
        if fetch != []:  # Here the programs checks that fetch is not just an empty list, as this would cause an index
                         # error, if the email address entered, didn't exist in the database, therefore returning an
                         # empty list, and the program attempted to index into that list
            fetch = list(fetch[0])  # fetch is converted from being a tuple to a list (when the function fetch is
                                    # carried out, it returns a list containing tuples), therefore here as only one user
                                    # will ever be returned it is stored at index location 0, and so that this tuple can
                                    # be manipulated and indexed, it has to be converted into a list.
            if fetch[3] == y[2]:  # The program then compares the contents of fetch[3] (the users
                                  # correct password which is stored in the database) with y[2], which is the user
                                  # entered password.
                return str([fetch[1],fetch[2]])  # The email address of the user is then returned to the constructor,
                                                 # as well as their name
            else:  # If the passwords don't match, FALSE is returned to the constructor
                return "FALSE"
        else: # If fetch returns an empty list, FALSE is returned to the constructor
            return "FALSE"

    def __new__(cls, y, z):
        flag = cls.check(y, z) # The SignIn function is created, passing through the parameters users inputted data and
                               # access to the database as y and z respectively
        return flag  # The result of flag is returned to the client, with the result being either the users email and
                     # name, or FALSE.

# The objects Register creates a new user within the database. Here data is validated to make sure that it doesn't
# already exist, and then added. The data required for Register is the users email, name and password. Once again this
# object uses the class method, in order for it's parent variable (response) to be able to store the data in which the
# object returns

class Register:
    @classmethod  # This is a function decorator and allows for methods contained within the class to be called
    def check(cls, y, z):  # The function check, is very similar to the check found in SignIn, albeit with this version
                           # being simpler, only desiring to determine whether the email address entered by the user
                           # exists in the database
        fetch = email_check(y[1], z)
        if fetch == []:  # The program then checks if fetch is a empty list, then this means that no user with the email
                         # address entered by the user exists within the database.
            create = cls.new_user(y, z)  # The function new_user is created, with the parameters y, z being passed
                                         # through
            return create  # The outcome of create is returned
        else:
            return "FALSE"  # FALSE is returned

    def new_user(y,z): # The function new_user, verifies that the email address entered is valid, as well as inserting
                       # valid data into the database
        welcome_email = codecs.open("Welcome.txt", "r", "utf-8")  # The text file, "Welcome.txt" is decoded and opened
        read_email = welcome_email.read()  # The text file is read
        welcome_email.close() # The text file is closed
        read_email = read_email.replace("NAME_OF_USER", y[2])  # The place holder NAME_OF_USER is replaced with the
                                                               # users name, which is held in the parameter as y[2]
        try:  # A try and except argument is used here in order to allow for emails to 'bounce back', which occurs
              # when an invalid email address is entered, causing a smtplib.SMTPRecipientsRefused error
            send_email(y[1], "Welcome", read_email)  # The procedure send_email is called, passing through the users
                                                     # email address, the subject title of "Welcome", and the
                                                     # customised html text with the users name in it. This email
                                                     # is sent before the database is updated in order to validate the
                                                     # email. If the recipient refuses the email, then it means that
                                                     # the exception clause is run, and the database isn't updated.
            z.cursor.execute("INSERT INTO csusers (Email, Name, Password) VALUES (%s, %s, %s)", (y[1], y[2], y[3]))
            # If the send_email procedure doesn't cause any errors, then the database is updated with the users email,
            # name and password which they entered.
            z.myDB.commit()  # The data is then committed to the database.
            return SignIn(['', y[1], y[3]], z)  # The SignIn object is created in order to return the same data required
                                                # for login. The parameters which are passed through contain a list,
                                                # formatted in the same way required by SignIn. Due to this, index 0 in
                                                # the list is essentially empty. The dictionary is also passed through
                                                # with parameter z. The result of this is then returned.
        except smtplib.SMTPRecipientsRefused:  # If the email 'bounces back', EMAIL FALSE is returned
            return "EMAIL FALSE"

    def __new__(cls, y, z):
        response = cls.check(y, z)  # The function is check is called, with the parameters y (containing the users data)
                                    # and z (containing the dictionary).
        return response  # response is then returned to the client

# The objects ChangePassword allows for a users password to be changed and updated within the database. ChangePassword
# is not an object within itself, but instead encapsulates related functions. This has been coded in this way to allow
# for the user to work through the steps required to change their password, at their own pace, instead of filling in
# a form with all the required details which are then sent to the server, which would allow for ChangePassword to be
# coded as an object. ChangePassword allows for the changing of a password if a user has forgotten their password, or
# if a user wishes to change their password

class ChangePassword:
    def send_reset_code(y, z): # When the function send_reset_code is called from the client, a reset code is generated
                               # and emailed to the user
        fetch = email_check(y[1],z) # As seen previously, email_check is used to verify the user who wishes to reset their
                                    # password exists
        if fetch == []:     # If the user doesn't exist, then the server returns FALSE to the client
            return "FALSE"
        else:  # If the user does exist 
            verification_code = random.randint(10000, 99999)  # A 5 digit random number is generated
            z.cursor.execute("UPDATE csusers SET ResetID='" + str(verification_code) + "' WHERE Email='" + y[1] + "'")
            # The 5 digit random number, verification code, is added to the database, updating the ResetID field relating
            # to the users email
            z.myDB.commit()  # The update is then saved to the database
            reset_email = codecs.open("ForgotPasswordEmail.txt", "r", "utf-8")  # As seen in Register.new_user, the
                                                                                # email text file is opened, read, closed
                                                                                # and here, the placeholder verification
                                                                                # code is changed to verification_code
                                                                                # (random number generated) converted to
                                                                                # a string, and the name of user is replaced.
                                                                                # The email customised email is then sent
            read_email = reset_email.read()
            reset_email.close()
            read_email = read_email.replace("VERIFICATION_CODE", str(verification_code))
            read_email = read_email.replace("NAME_OF_USER", fetch[0][2])
            send_email(y[1], "Verification Code", read_email)
            return "TRUE"  # TRUE is then returned to the client, confirming that a verification code has been sent

    def check_reset_code(y, z):  # The function check_reset_code verifies that the code entered by a user, is the
                                 # same as the code stored in the ResetID field with the correclating email address
        fetch = email_check(y[1],z)  # email_check is used to return the tuple with the correlating email address
        if y[2] == fetch[0][5]:  # If the reset code entered is the same as the one held in the database
            if y[2] == '':      # This checks to make sure both values aren't empty strings
                return "FALSE" # If both values are empty strings FALSE is returned
            else:
                return "TRUE" # If both reset codes match, then TRUE is returned
        else:
            return "FALSE" # If the codes don't match, FALSE is returned

    def update_password_reset(y, z):  # The function update_password_reset changes a users password within
                                      # the database
        fetch = ChangePassword.check_reset_code(y, z) # Here, the previous function, check_reset_code is called.
                                                      # This is to make sure that the details entered are the same
                                                      # as when they are previously verified, to ensure that
                                                      # the user doesn't have a free pass to change any users password
                                                      
        if fetch == "TRUE":  # If the verification code is correct for the user
            z.cursor.execute("UPDATE csusers SET Password='" + y[3] + "' WHERE Email='" + y[1] + "'")
            z.cursor.execute("UPDATE csusers SET ResetID='' WHERE Email='" + y[1] + "'")
            # The users password is updated, and the ResetID is set to a empty string
            z.myDB.commit() # The update is then saved to the database
            return SignIn(['', y[1], y[3]], z)  # As seen previously when a new user is made, the SignIn object is created
                                                # in order to return the same data required for login 
        else:  # If the details don't match, FALSE is returned
            return "FALSE"
    def update_password(y,z): # The function update_password is called by the client when a user wishes to change their
                              # password, and they know their current password
        fetch = SignIn(y, z) # The function SignIn is called, in order to verify that the user has entered their correct
                             # email and password
        if fetch == "FALSE": # If the password doesn't match the email, then FALSE is returned to the client
            return "FALSE"
        else: # If the details match
            z.cursor.execute("UPDATE csusers SET Password='" + y[3] + "' WHERE Email='" + y[1] + "'")
            z.myDB.commit()
            # The users password is updated within the database corresponding to the users email, and then this update
            # is saved to the database
            return SignIn(['', y[1], y[3]], z)  # As seen previously when a new user is made, the SignIn object is created
                                                # in order to return the same data required for login 
class GraphData:  # GraphData once again isn't coded as an object, but instead a collection of related function, to allow
                  # for the client to access specific functions when required. GraphData includes functions which are able
                  # to return the list of available forex, return a list of available forex with details of whether each
                  # forex is up or down, return data for a specific forex over a defined time period, or get the latest
                  # data on a forex.
    def fetch_columns(y,z): # The function fetch_columns, returns a list of all the available forex which are available to
                            # be traded on
        z.cursor.execute("SHOW COLUMNS FROM data")  # All columns are returned from the data table (each column in data is
                                                    # a forex)
        a = [] # a is defined as an empty list
        for r in z.cursor: # For each item in the database cursor
            if r[0] != 'date': # As long as the item isn't date
                a.append(r[0]) # The item is added to the list a
        return str(a) # The forex list is returned 
    def columns(y,z): # The function columns, expands on the previous function fetch_columns, creating a 2D list
                      # with the first value being the forex, and the second value being either 1 or 0, depending
                      # on whether the forex is up or down
        b = eval(GraphData.fetch_columns(y,z)) # The previous function, fetch_columns is called, in order to get
                                               # a list of the available forex markets
        z.cursor.execute("select date from data ORDER BY date DESC LIMIT 1") # The last update date is then retrieved
                                                                             # from the database
        for s in z.cursor:
            date = list(s)[0][:8] # The date (formatted to only store up to the 8th character so that the specific
                                  # time is removed. This will allow for the data only from the last update day to be
                                  # retrieved. The date is stored in the variable date
        complete = []  # complete is an empty list which will be used to store the data
        for r in b:  # For each forex in the list b
            z.cursor.execute("select " + r + " from data WHERE date LIKE '" + date + "%' ORDER BY date DESC LIMIT 1")
            # The forex data is retrieved where the date is similar to the variable date. This has been coded this way
            # due to the date is stored in the format YYYYMMDDHHMM. The variable date stores date as YYYYMMDD. Therefore,
            # when it's being requested from the database it's really saying, select (a forex) from data where data is
            # equal to YYYYMMDD and contains any HHMM after that. The values returned are then sorted in descending order
            # via their corresponding date, and the limit 1 means that the first item returned is selected, and returned
            # to z.cursor. In essence, it's returning the lastest value for a forex.
            for p in z.cursor:
                last = float(list(p)[0])  # The value returned is then stored as the variable last
            z.cursor.execute("select " + r + " from data WHERE date LIKE '" + date + "%' ORDER BY date ASC LIMIT 1")
            # This sql statement is partically identical apart from how the data is ordered. Instead of being ordered
            # by descending values of date, it's sorted by ascending values. This is to retrieve the first value of
            # the forex for the day
            for p in z.cursor:
                first = float(list(p)[0]) # The value returned is then stored as the variable first
            # Last is compared against first, in order to determine whether the forex has moved up single opening, or down
            if last > first: 
                up = 1
            if last == first:
                up = 0
            if last < first:
                up = -1
            complete.append([r, up]) # The forex, as well as it's state is added to the list complete, creating a 2d list
        return str(complete) # the complete forex list, along with it's counterpart state, is returned as a string
    # The function get_values, gets the entire data set for a certain forex, for a requested period of time
    def get_values(y,z):  
        if y[2] == 'today_data': # If the client includes today_data within their request
            a = list(eval(GraphData.get_latest(y,z))[0])  # The date is fetched from the database by finding the last entry
            b = a[0][:8] # The date is then formatted, to exclude HHMM
            z.cursor.execute("select date, " + y[1] + " from data WHERE date LIKE '"+b+"%'")
            # An sql statement is executed to fetch all date for the client desired index, where the date == YYYYMMDD and
            # any HHMM
        elif y[2] == 'current_data':  # If the client includes current_data within their request
            z.cursor.execute("SELECT DISTINCT LEFT(date, 8) FROM data ORDER BY date DESC LIMIT 8")
            # An sql statement is executed to return the last weeks worth of dates which are stored within the database.
            # This is accomplished by selecting the first 8 characters from the date field, and then ordering them in
            # descending order, and finally limiting the result to 8 dates
            a = "select date, "+y[1]+" from "+y[2]+" WHERE "  # A template for the next sql statement which will return
                                                              # all datapoints within the 8 dates for the specific forex
            # Iteration has been used here to append each date to the sql statement
            first = True
            for items in z.cursor:
                if first == True:
                    a += 'date LIKE "' + items[0] +'%"'
                    first = False
                else:
                    a += ' OR date LIKE "'+items[0]+'%"'
            z.cursor.execute(a) # The statement is then executed
        else:  # If the user requests historic_data 
            z.cursor.execute("select date, "+y[1]+" from data where date LIKE '______01%'") #All data points where
                                                                                            #the users forex MM = 01
                                                                                            #be returned
        # This section of the code retrieves the data from the cursor. As the data set here is rather large, it
        # exceeds the maximum packet size. To resolve this, data is split into chunks of length 2048 characters, which
        # are sent invidivually and reformatted on the client side
        complete_data = [] 
        for items in z.cursor:
            complete_data.append(items) # All data is retrieved and added to the list, complete_data
        low = 0 # Sets the starting index value for the split string 
        up = 2048 # Set the end index value value for the split string
        split_complete_data = []
        while True: # A while loop is used to itteratively split the list, with a break being called when this has been completed
            x = str(complete_data)[low:up] # Complete data is converted into a string, to allow for indexing by characters between
                                           # index low and index high
            if x!= '': # ie, if the range of the indexed list doesn't exceed the the amount of items in x, which would return an
                       # empty string
                split_complete_data.append(x)  # x is added to the list split_complete_data 
                low += 2048 # Both low and up are incremented by 2048 so the next packet can be created
                up += 2048
            else: # If the max length of the string x has been exceeded i.e there are no more values to add to split_complete_data
                split_complete_data.append('COMPLETE') # A tail string is added to the end, so the client knows when they have retrieved
                                                       # all the data
                break
        return split_complete_data # This list is then sent to the client
    def get_latest(y,z): # This function returns the latest data point for a specific forex
        z.cursor.execute("select date, "+y[1]+" from data ORDER BY date DESC LIMIT 1")
        # The sql statement selects the data and specified forex, which are then order by the data descending (lasted data is at top)
        # finally limiting the response to the last value by limiting it to 1
        data = []
        for items in z.cursor:
            data.append(items)  # The data from cursor is then stored in the list data
        return str(data) # This data is then returned
    
class Purchase:   # Purchase isn't coded as a object, but instead a collection of related function, to allow
                  # for the client to access specific functions when required. Purchase includes functions which are able
                  # to update the database with a trade, return a users trade data and close a trade
    def trade(y,z): # The procedure trade verifies the user is eligible to trade and procedues to process the trade if valid
        x  =  float(eval(Purchase.update_user_data(['',y[1]],z))[0]) # This gets the users available balance
        a = list(eval(GraphData.get_latest(['',y[3]], z))[0]) # This returns the datetime of the latestest forex update to the database
                                                              # i.e. the date of the of the specific forex
        if x >= float(y[4]):  # If the users available balance is greater than the amount the wish to purchase
            z.cursor.execute("INSERT INTO trades (user, type,  symbol, quantity, open_date) VALUES (%s, %s, %s, %s, %s)", (y[1], y[2], y[3],y[4],a[0]))
            # A sql statement is updated to reflect the users purchases
            z.myDB.commit()
            return 'True' # Returns true to the client, so the user knows the trade was completed
        else:
            return 'False' # Returns false to the client, so the user knows the trade couldn't be completed
    def return_userdata(y, z):  # The function return_userdata returns a list of open/closed trades, includinging the users investment, profit and percentage
        if y[2] == 'open': # If the client requests open trades
            z.cursor.execute("select trade_id, type, symbol, quantity, open_date from trades WHERE user = '" + y[1] + "' AND close_date is NULL")
            # An sql statement is executed selecting the values needed to calculate users investment, profit and the percentage profit on
            # an open trade
        else:
            z.cursor.execute("select trade_id, type, symbol, quantity, open_date, close_date from trades WHERE user = '" + y[
                1] + "' AND close_date IS NOT NULL")
            # An sql statement is executed selecting the values needed to calculate users investment, profit and the percentage profit on
            # an closed trade
        cur = []
        for x in z.cursor:
            cur.append(x) # Each tuple from the cursor is the added to the list cur
        trades = []
        trades_list = []
        for items in cur:
            z.cursor.execute("select " + items[2] + " from data WHERE date = '"+items[4]+"'")
            # This sql statement retrieves the data point of the forex for the date at which the trade was opened
            cur1 = []
            for x in z.cursor:
                cur1.append(x)
            l = list(items)
            l.append(l[4])
            l[4] = str(list(cur1[0])[0]) # The forex point is inserted into position 4 (this is so that when data is sent to
                                         # a function, it is sent in the right order. This is also why the item in position
                                         # 4 has been re-added to the end of the list
            if y[2]=='closed':  # If the forex is closed then the data point is retrieved at the point when it was closed
                z.cursor.execute("select " + items[2] + " from data WHERE date = '" + items[5] + "'")
                for x in z.cursor:
                    l.append(l[5])
                    l[5] = str(list(x)[0]) # Once again, the item in l[5] is moved to the end, in order to put the list
                                           # in the correct order for a later function, with l[5] being replaced with the
                                           # position 


            trades.append(tuple(l))# the list l is then converted to a tuple and added to trades
        for items in trades:  # For each item in trades, it determins whether where the currency that is being
                              # converted into is GBP (which is the programs base currency)
            if items[2][:3] != 'GBP':
                if y[2] == 'open':
                    # This converts the users quntatity into the base currency the user wishes to
                    #trade. example user wants to trade USDAUD, then program works out convesion rate between
                    #GBPUSD
                    z.cursor.execute("select GBP" + items[2][:3] + " from data WHERE date = '" + items[5] + "'")
                else: # Same applies to a closed trade, however the position is slightly alterered
                    z.cursor.execute("select GBP" + items[2][:3] + " from data WHERE date = '" + items[6] + "'")

                for x in z.cursor:
                    origin = float(list(x)[0]) # The conversion rate is then stored as the variable origin
            else:
                origin = 1 # If the first 3 characters of the forex are GBPUSD, then no convesrion is needed
                           # and origin created, storing the integer stored as 1
            print(items)
            print(origin)
            b = float(items[3]) * origin * float(items[4]) # Here the conversion is made into the currency selected and
                                                           # then multiplied by the quantity the user wants. This will
                                                           # be used in part to calculate profit/loss
            if y[2] == 'open': # If the trade is opened
                while 1:
                    try:
                        a = float(list(eval(GraphData.get_latest(items[1:], z))[0])[1]) # The latest data point is
                        # retrieved. This is in a while loop to prevent a TypeError from causing the program to break

                        break
                    except TypeError:
                        pass
                c = float(items[3]) * origin * float(a)  # Second conversion made. Conversion made into the same currency
                                                         # that user originally requested by using the latest data point
                                                         # that has just been retrieved. This is then multiplied by the
                                                         # quantity the user wants
            else:
                c = float(items[3]) * origin * float(items[5]) # If the trade is closed, then closing point will
                                                               # be included in the item, so no further data needs to be
                                                               # retrieved.

            if items[1] == 'Buy': # Depending on whether the trade was buying or selling depends on how profit/loss is
                                  # calculated
                if items[2][3:] != 'GBP': # This checks whether the 2 conversions that have been made have been into
                                          # GBP (the base currency for the program)

                    if y[2] == 'open': # If they haven't and the trade is open
                        profit = str("{0:.2f}".format((c - b) * float(list(eval(GraphData.get_latest(['',items[2][3:]+'GBP'], z))[0])[1]) ))
                        # variable profit is assigned to the calculated profit/loss of the trade. profit is calculated
                        # by determining the difference between the last conversion (c) and the first conversion (b) and
                        # then converting that difference into GBP. This is then formatted to 2 decimal places and
                        # converted to a string
                    if y[2] == 'closed': # If they haven't and the trade is closed
                        z.cursor.execute("SELECT " + items[2][3:]+ "GBP from data WHERE date = " + items[7])
                        for u in z.cursor:
                            profit = str("{0:.2f}".format((c - b) * float(list(u)[0])))
                        # same calculation occurs, however data point to convert from currency that it's b and c are
                        # currently is used from the data of which the trade was closed
                else:
                    profit = str("{0:.2f}".format(c - b)) # If b and c are already in GBP, then subtraction occurs
                    # followed by the conversion into a string

                percentage = str("{0:.2f}".format((1 - (b / c)) * 100)) #percentage profit is calculated and formatted


            else: # If it's a sell instead, everything is essentially the same apart from the calculation
                if items[2][3:] != 'GBP':
                    if y[2] == 'open':
                        profit = str("{0:.2f}".format((b-c) * float(list(eval(GraphData.get_latest(['',items[2][3:]+'GBP'], z))[0])[1]) ))
                        # Instead of c-b, it's b-c

                    if y[2] == 'closed':
                        z.cursor.execute("SELECT " + items[2][3:]+ "GBP from data WHERE date = " + items[7])
                        for u in z.cursor:
                            profit = str("{0:.2f}".format((b-c) * float(list(u)[0])))  # change applies here
                else:
                    profit = str("{0:.2f}".format(b-c)) # and here

                percentage = str("{0:.2f}".format((1 - (c/b)) * 100)) # Also, swapped around here also to calculate
                                                                      # percentage profit/loss
            investment = str("{0:.2f}".format(float(items[3]))) # Inital investment is saved as the vairable investment
                                                                # formatted to 2 decimal places
            trades_list.append([items[0], items[1], items[2], investment, profit, percentage, y[2]])
            # The trade is then added to the list with trade ID, buy or sell, forex, investment, profit/loss, percentage
            # profit/loss and whether it's open/closed


        return str(trades_list) # list is then returned
    def close(y,z):  # The function close, allows for a user to close a trade
        z.cursor.execute("SELECT symbol from trades WHERE trade_id ="+y[1]) # An sql statement is executed which returns that the symbol
                                                                            # for the trade that the user wishes to delete
        trade = ['']
        for item in z.cursor:
            trade.append(list(item)[0])
        a = list(eval(GraphData.get_latest(trade, z))[0])[0] # GraphData.get_latest is called to get the last update time (which will be
                                                             # the trade close time)
        z.cursor.execute("UPDATE trades SET close_date='" + a + "' WHERE trade_id='" + y[1] + "'") # Trade is then updated within the database
                                                                                                   # to add the close date stored as a
        z.myDB.commit()
        return 'TRUE' # True is returned to the user so they know that the trade has been successful

    def update_user_data(y, z):     # Update_user_data returns data about the user inlcuding: available, equity, profit, total_trades,
                                    # average_profit, greatest_profit
        z.cursor.execute("SELECT Initial_Value from csusers WHERE Email='" + y[1] + "'") # Here the users starting value (typically e.g
                                    # 100,000) is returned for the user
        for item in z.cursor:
            initial= list(item)[0] # The value from the database is then stored in the list initial
        while 1: 
            try:
                initial = float(initial) # The value from the database is then stored as a float in the variable inital. A while
                                            # loop has been used here with an exception clause, due to there being occassions where
                                            # a IndexError is raised. This was fixed by repeating the attempt to turn initial into
                                            # a float
                break
            except IndexError:
                pass
        # Below, lists are created which will store values which will stored, the profit from each open trade, each closed trade,
        # the total amount investested for each trade. With the variable total_trades being incremented for each trade the user
        # has completed. The list greatest, stores the greatest profit for both open and closed, with the greatest value in this
        # list calculated at the end
        total_open = []
        total_closed = []
        total_invested = 0
        total_trades = 0
        greatest = []
        open = eval(Purchase.return_userdata(['', y[1], 'open'], z)) # The variable open will store the returned list
                                                                     # from the function return_user data. 'open' is
                                                                     # sent in, to return a list of all the open trades
        try:
            for a in open:  # For each item in open, the fifth item (the profit) is added to the total_open list. The
                            # fourth item (invested for the trade) is added to total_invested and the total_trades is
                            # incremented by 1.
                total_open.append(float(a[4]))
                total_invested += float(a[3])
                total_trades += 1
            greatest.append(max(total_open)) # The greatest profit is then established by calculating the maximum value in
                                             # total_open
        except IndexError and OSError and ValueError: # If an exception is caused (due to there being no open trades) then
                                                      # 0 is added to the lists total_open and greatest
            total_open.append(float(0))
            greatest.append(float(0))

        closed = eval(Purchase.return_userdata(['', y[1], 'closed'], z)) # The variable closed will store the returned list
                                                                         # from the function return_user data. 'closed' is
                                                                         # sent in, to return a list of all the closed trades
        try: # Essentially, the above process is repeated, adding the values respective values to total_closed instead,
            # but also adding to total_trades. total_invested is not required as the trade is closed and therefore won't
            # affect their available balance
            for a in closed:
                total_closed.append(float(a[4]))
                total_trades += 1
            greatest.append(max(total_closed))
        except IndexError and OSError and ValueError:
            total_closed.append(float(0))
            greatest.append(float(0))
        available = ("{0:.2f}".format(initial + sum(total_closed) - total_invested)) # available is calculated by adding
                                                                                     # the sum of the profit of all their
                                                                                     # closed trades to their inital value
                                                                                     # (100000) and subtracting the total
                                                                                     # invested
        equity = ("{0:.2f}".format(initial + sum(total_open) + sum(total_closed)))   # equity is calculated by adding
                                                                                     # the sum of the profit of all their
                                                                                     # open and closed trades to their
                                                                                     # inital value (100000)
        profit = ("{0:.2f}".format(sum(total_open) + sum(total_closed))) # profit is calculated by adding sum of all open
                                                                         # closed trade profits
        if total_trades != 0:
            average_profit = ("{0:.2f}".format(float(profit)/total_trades)) # If the users total trades aren't 0 then
            # average profit is calculated
        else:
            average_profit = "0.00" # If it is there average profit is 0

        greatest_profit = ("{0:.2f}".format(max(greatest))) # greatest profit is decided between the bigger value in the
                                                            # greatest list

        if float(equity) + float(profit) < 0: # If a users equity and their profit falls below 0 then their account will
                                              # be reset
            z.cursor.execute("DELETE FROM trades WHERE user='" + y[1] + "'") # the users trades will be deleted from the
                                                                             # database
            z.myDB.commit()
            fetch = email_check(y[1], z) # Users name will be found
            reset_account_email = codecs.open("ResetAccountEmail.txt", "r", "utf-8")  # reset email will tell user what has
                                                                                      # happened. Here it is opened
            read_email = reset_account_email.read()
            reset_account_email.close()
            read_email = read_email.replace("NAME_OF_USER", fetch[0][2]) # users name is  inserted
            send_email(y[1], "Account Reset", read_email) # email is sent
            return 'Reset' # 'Reset' is sent to client so its aware that users account has been reset
        return str([available, equity, profit, total_trades, average_profit, greatest_profit]) # values are returned to client
def delete_account(y , z):  # Delete account is coded as a function for simplicity. Delete account removes all user
                            # data from the database. It requires both the users email address and password to verify
                            # that it is a genuine request.
        x = SignIn(y,z) # Users credentials are used to login in to verify the user
        if x != "FALSE": # If SignIn does not return false, but instead the user credentials then
            fetch = email_check(y[1], z) # email_check is used to return the users name, for use in an email
            z.cursor.execute("DELETE FROM trades WHERE user='" + y[1] + "'") # All the users trades are deleted from the
                                                                             # trades tables
            z.cursor.execute("DELETE FROM csusers WHERE Email='" + y[1] + "'") # User is deleted from the csusers table
            z.myDB.commit() # Changes are saved to the database
            delete_email = codecs.open("DeleteEmail.txt", "r", "utf-8") # DeleteEmail.txt is opened and the users name
                                                                        # is inserted where NAME_OF_USER
            read_email = delete_email.read()
            delete_email.close()
            read_email = read_email.replace("NAME_OF_USER", fetch[0][2])
            send_email(y[1], "Account Deletion - Confirmation", read_email) # Email is sent
            return 'TRUE' # True is returned to the client so that it knows that the account has been deleted
        else: # If credentials are invalid, then false is returned to the user so that its aware that the account has
              # not been deleted
            return 'FALSE'
