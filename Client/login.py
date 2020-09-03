from tkinter import*
from tkinter import messagebox
import socket
def move_to_forex(response):
        import home
        ParentObjects.root.geometry("1000x600")
        ParentObjects.root.config(bg='#2c2d37')
        userdata = ['David Golding', 20000, 20000, 0]
        about_image = PhotoImage(file="about_image4.gif").subsample(2)
        #response.append(20000)
        #response.append(20000)
        #response.append(0)
        home.ParentObjects(ParentObjects.root)
        home.ParentObjects.user = response
        home.Connection()
        home.Connection.s = Connection.s
        home.update_user_data(home.ParentObjects.user[0])
        home.UserInfo(home.ParentObjects.user)
        home.MenuBar()
        home.ForexScreen()
class Connection:
    def send(x):
        Connection.s.send(x.encode())
        recieved = Connection.s.recv(1024).decode()
        return recieved
    def start():
        ParentObjects.parent_login.pack_forget()
        ParentObjects.parent_login = Frame(ParentObjects.father, bg='#2c2d37')
        createLogin = SignIn()
        try:
            host = '0.0.0.0'
            port = 2222
            Connection.s.connect((host, port))
            createLogin.success()
        except ConnectionRefusedError:
            createLogin.failed()
    def __new__(cls):
        cls.s = socket.socket()

                                                   

class tkEntry:
        @classmethod
        def focus(cls, y, z):
            if z[y][1] == 0:
                y.delete(0, "end")
                change = ['Password', 'Confirm Password', 'New Password', 'Current Password']
                if z[y][0] in change:
                    y.config(show="*")
                y.config(fg='white')
                z[y][1] = 1

        @classmethod
        def notfocus(cls, y, z):
            if y.get() == '':
                change = ['Password', 'Confirm Password', 'New Password', 'Current Password']
                if z[y][0] in change:
                    y.config(show="")
                y.insert(0, z[y][0])
                y.config(fg='white')
                z[y][1] = 0

        def __new__(cls, x, y, z):
            a = Entry(x, highlightthickness=0.5, bd=0, justify=CENTER)
            z.update({a: [y, 0]})
            a.config(fg='white')
            a.insert(0, z[a][0])
            a.bind('<FocusIn>', lambda event: cls.focus(a, z))
            a.bind('<FocusOut>', lambda event: cls.notfocus(a, z))
            return a
class tkButton:
        def enter(self,frame, label, colour):
                frame.configure(highlightbackground=colour, highlightcolor=colour)
                label.configure(fg=colour)
        def leave(self,frame, label, colour):
                frame.configure(highlightbackground=colour, highlightcolor=colour)
                label.configure(fg=colour)
        def cget(self,x):
            return self.b.cget(x)
        def config(self, x):
                self.b.bind('<Button-1>', x)
        def config_text(self, x):
                self.b.config(text = x)
        def pack(self,**args):
                self.a.pack(**args)
        def pack_forget(self):
                self.a.pack_forget()
        def __init__(self, frame, data, task, coloura, colourb):
                self.a = Frame(frame, highlightbackground=coloura, highlightcolor=coloura, highlightthickness=1)
                self.b = Label(self.a, text = data, fg=coloura, bg=frame.cget("bg"), width = 10)
                self.b.pack()
                self.b.bind('<Button-1>',task)
                self.a.bind("<Enter>", lambda event: self.enter(self.a,self.b, colourb))
                self.a.bind("<Leave>", lambda event: self.leave(self.a,self.b, coloura))
class ParentObjects:
    def loadLogin(cls):
        cls.parent_register.pack_forget()
        cls.parent_login.pack(expand=1)
        cls.register.config(font="Helvetica 13 ")
        cls.logIn.config(font = "Helvetica 13 bold")
        ParentObjects.root.title("Login - Virtual Trading")
        cls.father.config(bg ='#2c2d37')
        ParentObjects.statusLabelpos.config(bg ='#2c2d37')
    def loadRegister(cls):
        cls.parent_login.pack_forget()
        cls.parent_register.pack(expand=1)
        cls.register.config(font="Helvetica 13 bold")
        cls.logIn.config(font = "Helvetica 13")
        ParentObjects.root.title("Register - Virtual Trading")
        cls.father.config(bg ='#111111')
        ParentObjects.statusLabelpos.config(bg ='#111111')
        if cls.register_activated == 0:
            Register()
            cls.register_activated = 1
    def help():
        help = Tk()
        help.attributes('-topmost', True)
        help.geometry('600x300')
        help.title("About - Virtual Trading")
        T0 = Text(help, bg='#2c2d37', highlightbackground='#2c2d37')
        T0.pack(expand = 1, fill = BOTH)
        # font=('Arial', 12, 'bold', 'italic'),
        T0.tag_configure('bold', justify='center', font=('Verdana', 20, 'bold'), foreground='white'.capitalize())
        T0.tag_configure('normal', font=('Tempus Sans ITC', 12), justify='left', foreground='white')
        T0.tag_configure('title', font=('Tempus Sans ITC', 12), justify='left', foreground='white',underline=True)

        T0.insert(END, "Virtual Trading - Version 1.0\n", 'bold')
        T0.insert(END, "Getting Started:", 'title')
        T0.insert(END, "\nTo use Virtual Trading you first need to create an account. You can do this by pressing the register button on the login screen.  Once here you'll be prompted to enter your details. These include your name, email address, password and confirmation of your password. Your email address must be valid, and your password must be 6 characters or longer. Once these details have been validated, you will be given access to Virtual Trading, and you will be sent a welcome email.\n ", 'normal')
        T0.insert(END, "\nLogin:", 'title')
        T0.insert(END,
                  "\nTo login, simply use the email and password you used when you created your account. If you are unable to remember your password, you will have the opportunity to reset it. To do this, simply enter your email address, along with a password, in order to be prompted to reset your password. Once accepted the forgot password prompt, you will be taken to a screen to confirm your email address. Once confirmed, an email containing a verification code will be sent to you, and a screen will load which asks for this code. Once this code is confirmed, you will prompted to enter a new password, which must be 6 characters or longer. Finally your password will be updated, and you will be granted access to the system.\n ",
                  'normal')
        T0.insert(END, "\nTrading:", 'title')
        T0.insert(END, "\nOnce your credentials have been verified, the application will retrieve the necessary data from the server. This includes the available Forex (foreign exchange) list available to be traded on, the state of each available symbol, and your personal data\n ",'normal')

        T0.insert(END, "\nTroubleshooting:", 'title')
        T0.insert(END, "\nIf an issue arises while using Virtual Trading, try restarting the application. This will reset your connection with the Virtual Trading Server.\n ", 'normal')
        T0.config(state=DISABLED)

    def __new__(cls, root):
        cls.root = root
        cls.father = Frame(root)
        cls.father.pack(fill=BOTH, expand=1)
        cls.outerFrame = Frame(cls.father, bg='#2c2d37')
        cls.leftFrame = Frame(cls.outerFrame, bg='#2c2d37', padx=10, pady=10)
        cls.leftFrame.bind('<Button-1>', lambda event:cls.loadLogin(cls))
        cls.leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
        cls.rightFrameParent = Frame(cls.outerFrame, bg='#111111')
        cls.rightFrameParent.pack(side=RIGHT, fill=BOTH, expand=1)
        cls.rightFrame = Frame(cls.rightFrameParent, bg='#111111')
        cls.rightFrame.pack(expand=1)
        cls.parent_login = Frame(cls.father, bg = '#2c2d37')
        cls.parent_register = Frame(cls.father, bg = '#111111')
        cls.parent_forgot = Frame(cls.father, bg = '#2c2d37')
        cls.rightFrameParent.bind('<Button-1>', lambda event:cls.loadRegister(cls))
        cls.logIn = Label(cls.leftFrame, text="Log In",font="Helvetica 13 bold", bg = '#2c2d37', fg = 'white')
        cls.logIn.pack()
        cls.placeholder_dictionary = {}
        cls.register = Label(cls.rightFrame, text="Register", font="Helvetica 13", bg = '#111111', fg = 'white')
        cls.register.pack()
        cls.statusLabelpos = Label(ParentObjects.father, text='Server is reachable :D', fg = '#2db053', bg = '#2c2d37')
        menubar = Menu(root)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=cls.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", \

                             command=lambda: \
                                 cls.root.focus_get().event_generate('<<Cut>>'))
        editmenu.add_command(label="Copy", \
                             command=lambda: \
                                 cls.root.focus_get().event_generate('<<Copy>>'))
        editmenu.add_command(label="Paste", \
                             command=lambda: \
                                 cls.root.focus_get().event_generate('<<Paste>>'))
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=cls.help)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        root.config(menu=menubar)

        cls.register_activated = 0

class SignIn:           
    def success(self):
        ParentObjects.root.title("Login - Virtual Trading")
        ParentObjects.outerFrame.pack(side=TOP, fill=X)
        ParentObjects.parent_login.pack(expand=1)
        self.logoLabel.pack(pady=2)
        self.emailEntry.pack(pady=2)
        self.passwordEntry.pack(pady=2)
        self.loginButton.pack(pady=2)
        ParentObjects.statusLabelpos.pack(side=BOTTOM)
        
    def failed(self):
        ParentObjects.root.title("Offline - Virtual Trading")
        ParentObjects.parent_login.pack(expand=1)
        self.logoLabel.pack(pady=2)
        self.statusLabelneg.pack()
        self.retryButton.pack()
        
    def test_credentials(self, email, password):
        if email.get() == '' or ParentObjects.placeholder_dictionary[email][1] == 0:
            messagebox.showerror(title='Email Error',message = 'Please enter your email address.')
        else:
            if password.get() == '' or ParentObjects.placeholder_dictionary[password][1] == 0:
                messagebox.showerror(title='Password Error', message='Please enter your password.')
            else:
                self.test = self.send_credentials(email.get(), password.get())
                if self.test == True:
                        self.passwordEntry.delete(0,END)
                        tkEntry.notfocus(self.passwordEntry, ParentObjects.placeholder_dictionary)
                        ResetPassword(email.get())

                    
    def send_credentials(self, y, z):
        data = str(['SignIn', y, z])
        response = Connection.send(data)
        if response == "FALSE":
            reset = messagebox.askyesno("Error",
                                        "The username or password you have entered is incorrect. Do you wish to reset your password?")
            return reset
        else:
            ParentObjects.father.pack_forget()
            move_to_forex(eval(response))
            #####CLEAR SCREEN#####
                    
    def __init__(self):                       
        ParentObjects.father.config(bg ='#2c2d37')
        self.logoImage = PhotoImage(file="stock.gif")
        self.logoLabel = Label(ParentObjects.parent_login, bg='#2c2d37', image=self.logoImage)
        self.emailEntry = tkEntry(ParentObjects.parent_login, 'Email', ParentObjects.placeholder_dictionary)
        self.emailEntry.config(highlightbackground='#111111', bg='#2c2d37')
        self.passwordEntry = tkEntry(ParentObjects.parent_login, 'Password', ParentObjects.placeholder_dictionary)
        self.passwordEntry.config(highlightbackground='#111111', bg='#2c2d37')

        self.loginButton = tkButton(ParentObjects.parent_login, 'Submit', lambda event: self.test_credentials(self.emailEntry,self.passwordEntry), '#2db053', '#FFFFFF')
        self.statusLabelneg = Label(ParentObjects.parent_login, text="Can't reach server :(", fg='red', bg='#2c2d37')
        self.retryButton = tkButton(ParentObjects.parent_login, 'Retry', lambda event: Connection(), '#2db053', '#FFFFFF')
class ResetPassword:
        def backScreen(self):
                self.back.pack_forget()
                ParentObjects.parent_forgot.pack_forget()
                ParentObjects.outerFrame.pack(side=TOP, fill=X)
                ParentObjects.parent_login.pack(expand = 1)
                ParentObjects.root.title('Login - Virtual Trading')
        def confirm_email(self, email):
                    if email.get() == '' or ParentObjects.placeholder_dictionary[email][1] == 0:
                            messagebox.showerror(title='Email Error',message = 'Please enter your email address.')
                    else:
                        data = str(['ChangePassword.send_reset_code', email.get()])
                        response = Connection.send(data)
                        if response == 'TRUE':
                                self.emailEntry.pack_forget()
                                self.submit.pack_forget()
                                self.vcode.pack(pady=5)
                                self.submit.pack(pady=10)
                                self.submit.config(lambda event: self.confirm_code(email.get(),self.vcode))
                        else:
                                messagebox.showerror("Invalid", "This email address isn't registered with us :(")
        def confirm_code(self, email, verify):
                if verify.get() == '' or ParentObjects.placeholder_dictionary[verify][1] == 0:
                            messagebox.showerror(title='Code Error',message = 'Please enter your verification code.')
                else:
                        data = str(['ChangePassword.check_reset_code', email, verify.get()])
                        response = Connection.send(data)
                        if response == 'TRUE':
                                self.vcode.pack_forget()
                                self.submit.pack_forget()
                                self.passa.pack(pady=5)
                                self.passb.pack(pady=5)
                                self.submit.pack(pady=10)
                                self.submit.config(lambda event: self.new_password(email,self.vcode.get(),self.passa.get(),self.passb.get()))
                        else:
                                messagebox.showerror("Invalid", "The reset code you have entered is incorrect!")
        
        def new_password(self, email, verify, passa, passb):
            if passa == passb and len(passa) > 5:
                data = str(['ChangePassword.update_password_reset', email, verify, passa])
                response = Connection.send(data)
                if response == 'FALSE':
                    messagebox.showerror("Error", "Reset failed. Maybe try again later o.O")
                else:
                    ParentObjects.father.pack_forget()
                    move_to_forex(eval(response))
                    messagebox.showerror("Hell Yer!", "Password has been reset successfully B)")
            else:
                if passa != passb:
                    messagebox.showerror("Error", "The passwords you entered doesn't match :|")
                elif len(passa) < 6:
                    messagebox.showerror("Error", "Your password must be at least 6 characters long :P")
                    
        def __init__(self,email):
            ParentObjects.parent_forgot = Frame(ParentObjects.father, bg = '#2c2d37')
            ParentObjects.parent_login.pack_forget()
            ParentObjects.outerFrame.pack_forget()
            ParentObjects.parent_forgot.pack(expand = 1)
            ParentObjects.root.title('Reset Password - Virtual Trading')
            self.emailLabel = Label(ParentObjects.parent_forgot, text = 'Reset Password', font="Helvetica 14 bold", bg='#2c2d37', fg = 'white')
            self.emailLabel.pack(pady=5)
            self.emailEntry = tkEntry(ParentObjects.parent_forgot, 'Email', ParentObjects.placeholder_dictionary)
            self.emailEntry.config(highlightbackground='#111111', bg='#2c2d37')
            self.emailEntry.delete(0,END)
            self.emailEntry.insert(0,email)
            self.emailEntry.pack(pady=5)
            ParentObjects.placeholder_dictionary[self.emailEntry][1] = 1
            self.vcode = tkEntry(ParentObjects.parent_forgot, 'Verification Code', ParentObjects.placeholder_dictionary)
            self.vcode.config(highlightbackground='#111111', bg='#2c2d37')
            self.passa = tkEntry(ParentObjects.parent_forgot, 'New Password', ParentObjects.placeholder_dictionary)
            self.passa.config(highlightbackground='#111111', bg='#2c2d37')
            self.passb = tkEntry(ParentObjects.parent_forgot, 'Confirm Password', ParentObjects.placeholder_dictionary)
            self.passb.config(highlightbackground='#111111', bg='#2c2d37')
            self.submit = tkButton(ParentObjects.parent_forgot, 'Submit', lambda event: self.confirm_email(self.emailEntry), '#2db053', '#FFFFFF')
            self.submit.pack(pady=10)
            self.back = tkButton(ParentObjects.father, 'Back',lambda event:self.backScreen(), 'grey', '#FFFFFF')
            self.back.pack(pady=2)
       
class Register:
    def register_check(self, name, email, passa, passb):
        a = {name:['Name Error', 'Please enter your name.'], email:['Email Error', 'Please enter your email.'],
             passa:['Password Error', 'Please enter your password.'], passb:['Confirm Password Error', 'Please confirm your password.']}
        flag = 0
        for b in a:
            if b.get() == '' or ParentObjects.placeholder_dictionary[b][1] == 0:
                messagebox.showerror(title=a[b][1], message=a[b][1])
                flag = 1
                break
        if flag == 0:
            if passa.get() == passb.get() and len(passa.get()) > 5:
                data = str(['Register', email.get(),name.get(), passa.get()])
                response = Connection.send(data)
                if response == 'FALSE':
                    messagebox.showerror("Error", "Email address is already registered :S")
                elif response == 'EMAIL FALSE':
                    messagebox.showerror("Error", "Email address is not valid :S")
                else:
                    ParentObjects.father.pack_forget()
                    move_to_forex(eval(response))
                    messagebox.showerror("Hell Yer!", "Welcome to Virtual Trading :D")
            else:
                if passa.get() != passb.get():
                    messagebox.showerror("Error", "The passwords you have entered doesn't match :|")
                elif len(passa.get()) < 6:
                    messagebox.showerror("Error", "Your password must be at least 6 characters long :P")


    def __init__(self):
        ParentObjects.father.config(bg ='#111111')
        self.credentials = Label(ParentObjects.parent_register, text="Your Credentials:", font="Helvetica 14 bold",bg='#111111', fg = 'white')
        self.nameEntry = tkEntry(ParentObjects.parent_register, 'Name', ParentObjects.placeholder_dictionary)
        self.nameEntry.config(highlightbackground='#2c2d37', bg='#111111')
        self.emailNewEntry = tkEntry(ParentObjects.parent_register, 'Email', ParentObjects.placeholder_dictionary)
        self.emailNewEntry.config(highlightbackground='#2c2d37', bg='#111111')
        self.passwordNewEntry = tkEntry(ParentObjects.parent_register, 'Password', ParentObjects.placeholder_dictionary)
        self.passwordNewEntry.config(highlightbackground='#2c2d37', bg='#111111')
        self.passwordConfirm = tkEntry(ParentObjects.parent_register, 'Confirm Password', ParentObjects.placeholder_dictionary)
        self.passwordConfirm.config(highlightbackground='#2c2d37', bg='#111111')
        self.registerButton = tkButton(ParentObjects.parent_register, 'Register', lambda event: self.register_check(self.nameEntry, self.emailNewEntry, self.passwordNewEntry, self.passwordConfirm), '#2db053', '#FFFFFF')
        self.credentials.pack(pady = 2)
        self.nameEntry.pack(pady = 2)
        self.emailNewEntry.pack(pady = 2)
        self.passwordNewEntry.pack(pady = 2)
        self.passwordConfirm.pack(pady = 2)
        self.registerButton.pack(pady=2)

if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x600")
    #root.wm_attributes('-fullscreen', 'true')
    ParentObjects(root)
    Connection()
    Connection.start()
    root.mainloop()
