from tkinter import*
from tkinter import messagebox

import socket

import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")
matplotlib.rcParams['xtick.color'] = 'white'
matplotlib.rcParams['ytick.color'] = 'white'
def move_to_login():
    ParentObjects.father_frame.pack_forget()
    ParentObjects.root.geometry("1000x600")
    import login
    login.ParentObjects(ParentObjects.root)
    login.ParentObjects.root = ParentObjects.root
    login.Connection()
    login.Connection.s = Connection.s
    createLogin = login.SignIn()
    createLogin.success()
def update_user_data(user):
    data = str(['Purchase.update_user_data', user])
    response = Connection.send(data)
    if response == 'Reset':
        update_user_data(user)
        messagebox.showerror('Error',
                             "Unfortunately, your Equity - Profit has become less than £0.00. Your account has therefore been reset.")
    else:
        response = eval(response)
        ParentObjects.available.set('Available: £'+response[0])
        ParentObjects.equity.set('- Equity: £'+response[1])

        if float(response[2])<0:
            ParentObjects.profit.set('- Loss: £'+response[2][1:])
        else:
            ParentObjects.profit.set('- Profit: £' + response[2])
        if float(response[3]) == 1:
            ParentObjects.trades.set("You've made 1 trade")
        else:
            ParentObjects.trades.set("You've made " + str(response[3]) + " trades")
        if float(response[4]) < 0:
            ParentObjects.average.set("Your average loss is £"+str(response[4])[1:])
        else:
            ParentObjects.average.set("Your average profit is £" + str(response[4]))
        if float(response[5]) < 0:
            ParentObjects.greatest.set("Your smallest loss is £" + str(response[5])[1:])
        else:
            ParentObjects.greatest.set("Your greatest profit is £" + str(response[5]))


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
class ParentObjects:
    
    def __new__(cls, root):
        cls.root = root
        cls.user = ''
        cls.root.geometry("1200x800")
        cls.root.title("Loading Forex - Virtual Trading")
        cls.loading_frame = Frame(cls.root, bg='#2c2d37')
        cls.loading_frame.pack(fill=BOTH, expand=1)
        Label(cls.loading_frame, text = 'Loading ...',font="Helvetica 14 bold", bg='#2c2d37', fg = 'white').pack(expand = 1)
        cls.root.update()
        cls.father_frame = Frame(cls.root, bg='#2c2d37')
        #cls.father_frame.pack(fill=BOTH, expand=1)
        cls.menu_frame = Frame(cls.father_frame)
        cls.menu_frame.pack(side=LEFT, fill=BOTH, expand=0)
        cls.main_contents_frame = Frame(cls.father_frame)
        cls.main_activated = 0
        cls.placeholder_dictionary = {}
        cls.purchases_frame = Frame(cls.father_frame)
        cls.purchases_activated = 0
        cls.account_frame = Frame(cls.father_frame)
        cls.account_activated = 0
        cls.about_image = PhotoImage(file="about_image4.gif").subsample(2)
        cls.available = StringVar()
        cls.equity = StringVar()
        cls.profit = StringVar()
        cls.trades = StringVar()
        cls.average = StringVar()
        cls.greatest = StringVar()


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
                self.b = Label(self.a, text = data, fg=coloura, bg=frame.cget("bg"))
                self.b.pack()
                self.b.bind('<Button-1>',task)
                self.a.bind("<Enter>", lambda event: self.enter(self.a,self.b, colourb))
                self.a.bind("<Leave>", lambda event: self.leave(self.a,self.b, coloura))


class UserInfo:
    def pack(self):
        self.user_info_frame.pack(fill=X, side = TOP)
        self.user_info_spacer.pack(side=LEFT, fill=Y, expand=0)
        self.user_info_spacer0.pack(side=BOTTOM, fill=X, expand=0)
        self.user_info_data_frame.pack(side=LEFT, fill=BOTH, expand=1)
        self.user_info_spacer1.pack(side=LEFT, fill=Y, expand=0)
        self.user_info_spacer2.pack(side=LEFT, fill=Y, expand=0)
        self.user_info_name_frame.pack(side=RIGHT, fill=X, expand=0)
        #self.user_info_data_label.pack(side=LEFT, fill=BOTH, expand=1)
        self.f.pack()
        self.fa.pack(side = LEFT, fill = X, expand = 1)
        self.fb.pack(side = LEFT, fill = X, expand = 1)
        self.fc.pack(side = RIGHT, fill = X, expand = 1)
        self.available_b.pack(side = LEFT, anchor=E, padx = 0, ipadx = 0)
        self.equity_b.pack(side = LEFT, anchor=E, padx = 0, ipadx = 0)
        self.profit_b.pack(side = RIGHT, anchor=W, padx = 0, ipadx = 0)
        self.user_info_name_label.pack(side=RIGHT, fill=X, expand=0)

    def __init__(self, userdata):
        self.user_info_frame = Frame(ParentObjects.father_frame, bg='grey')
        self.user_info_spacer = Frame(self.user_info_frame, bg='#111111')
        self.user_info_spacer0 = Frame(self.user_info_frame, bg='#111111', width=30)
        self.user_info_data_frame = Frame(self.user_info_frame, bg='#2c2d37', height=30)
        self.user_info_spacer1 = Frame(self.user_info_data_frame, bg='#2c2d37')
        self.user_info_spacer2 = Frame(self.user_info_frame, bg='#111111')
        self.user_info_name_frame = Frame(self.user_info_frame, bg='light blue', height=30, width=250)
        self.f = Frame(self.user_info_data_frame,bg='#2c2d37', width = 70)
        self.fa = Frame(self.f)
        self.available_b = Label(self.fa,textvariable = ParentObjects.available ,font="Helvetica 14 ",
                                         bg='#2c2d37', fg='white')
        self.fb = Frame(self.f)
        self.equity_b = Label(self.fb,textvariable = ParentObjects.equity ,font="Helvetica 14 ",
                                         bg='#2c2d37', fg='white')
        self.fc = Frame(self.f)
        self.profit_b = Label(self.fc,textvariable = ParentObjects.profit ,font="Helvetica 14 ",
                                         bg='#2c2d37', fg='white')

        usertext = 'User: ' + userdata[1]
        self.user_info_name_label = Label(self.user_info_name_frame, text=usertext, font="Helvetica 14", width=25,
                                         bg='#2c2d37', fg='white')
        self.pack()


class MenuBar:

    def load_forex(self):
        update_user_data(ParentObjects.user[0])
        self.menu_forex_label.config(bg='#111111')
        self.menu_purchases_label.config(bg='#2c2d37')
        self.menu_account_label.config(bg='#2c2d37')
        ParentObjects.purchases_frame.pack_forget()
        ParentObjects.account_frame.pack_forget()
        ParentObjects.main_contents_frame.pack(fill = BOTH, expand = 1)
    def load_purchases(self):
        update_user_data(ParentObjects.user[0])

        ParentObjects.root.title("Purchases - Virtual Trading")
        self.menu_forex_label.config(bg='#2c2d37')
        self.menu_purchases_label.config(bg='#111111')
        self.menu_account_label.config(bg='#2c2d37')
        ParentObjects.main_contents_frame.pack_forget()
        ParentObjects.account_frame.pack_forget()
        ParentObjects.purchases_frame.pack_forget()
        PurchasesScreen()
        # x = PurchasesScreen()
        # if ParentObjects.purchases_activated == 0:
        #     PurchasesScreen()
        #     ParentObjects.purchases_activated = 1
        # else:
        #     ParentObjects.purchases_frame.pack(fill = BOTH, expand = 1)
    def load_account(self):
        update_user_data(ParentObjects.user[0])

        ParentObjects.root.title("Account - Virtual Trading")
        self.menu_forex_label.config(bg='#2c2d37')
        self.menu_purchases_label.config(bg='#2c2d37')
        self.menu_account_label.config(bg='#111111')
        ParentObjects.main_contents_frame.pack_forget()
        ParentObjects.purchases_frame.pack_forget()
        if ParentObjects.account_activated == 0:
            AccountScreen()
            ParentObjects.account_activated = 1
        else:
            ParentObjects.account_frame.pack(fill=BOTH, expand=1)
    def __init__(self):
        self.menu_forex_label = Label(ParentObjects.menu_frame, text='Forex', font="Helvetica 14 bold italic ", width=15, bg='#111111', fg = 'white')
        self.menu_forex_label.pack(fill=BOTH, expand=1)
        self.menu_forex_label.bind('<Button-1>', lambda event: self.load_forex())

        self.menu_live_stocks_spacer1 = Frame(ParentObjects.menu_frame, bg='#111111')
        self.menu_live_stocks_spacer1.pack(fill=X, expand=0)

        self.menu_purchases_label =Label(ParentObjects.menu_frame, text='Purchases', font="Helvetica 14 bold italic ", width=15, bg='#2c2d37',fg = 'white')
        self.menu_purchases_label.pack(fill=BOTH, expand=1)
        self.menu_purchases_label.bind('<Button-1>', lambda event:self.load_purchases())

        self.menu_live_stocks_spacer2 = Frame(ParentObjects.menu_frame, bg='#111111')
        self.menu_live_stocks_spacer2.pack(fill=X, expand=0)

        self.menu_account_label = Label(ParentObjects.menu_frame, text='Account', font="Helvetica 14 bold italic ", width=15, bg='#2c2d37', fg = 'white')
        self.menu_account_label.pack(fill=BOTH, expand=1)
        self.menu_account_label.bind('<Button-1>', lambda event:self.load_account())


class NavigationToolbar(NavigationToolbar2TkAgg):
    def set_message(self, msg):
        pass
    toolitems = [t for t in NavigationToolbar2TkAgg.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]
class create_graph:
    def get_data(self, column, command):
        self.complete = ''
        data  = str(['GraphData.get_values', column, command])
        Connection.s.send(data.encode())
        while True:
            data = Connection.s.recv(2048).decode()
            if 'COMPLETE' in data:
                break
            else:
                self.complete+=data
        self.complete = eval(self.complete)
    def xy(self, command, value):
        for x in self.complete:
            try:
                self.yList.append(float(x[1]))
                self.xList.append(str(x[0]))
                self.labels.append('')
                if command=='historic_data' and str(x[0])[2:4] not in self.historic_data :
                    self.historic_data.append(str(x[0])[2:4])
                if command == 'current_data' and str(x[0])[6:8]+'/'+str(x[0])[4:6]+'/'+str(x[0])[2:4] not in self.current_data:
                    self.current_data.append(str(x[0])[6:8]+'/'+str(x[0])[4:6]+'/'+str(x[0])[2:4])
                if command == 'today_data' and  x[0][8:10]+':00' not in self.today_data:
                    self.today_data.append(x[0][8:10]+':00')

            except TypeError:
                pass
        if command == 'today_data':
            self.opening = float(self.yList[0])
            updown = round((((self.yList[-1]/self.opening)-1)*100),4)
            t = str(self.yList[-1])+ ' ('+str(updown)+'%)'
            if updown > 0:
                value.config(text = t, fg = 'green')
            elif updown == 0:
                value.config(text=t, fg='white')
            else:
                value.config(text=t, fg='red')
    def xlabels(self, command):
        s = (len(self.labels) / len(command))
        z = s / 2
        e = len(command)
        for values in command:
            self.labels[int(z)] = values
            z += s
    def show(self, command):

        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=TOP, fill = BOTH, expand = 1)
        self.canvas._tkcanvas.config(bg='#2c2d37')
        self.canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand = 1)
        self.a.set_facecolor('#111111')
        self.a.grid(color='#2c2d37')
        self.a.plot(self.xList, self.yList, color='#2db053')
        #self.a.margins(0)
        self.a.set_ylabel("Rate", color="white")
        if command == 'historic_data':
            self.a.set_xlabel("Year", color="white")
        if command == 'current_data':
            self.a.set_xlabel("Day", color="white")
        if command == 'today_data':
            self.a.set_xlabel("Time", color="white")
        self.a.set_xticklabels(self.labels)

    def __init__(self, frame, column, command, value):
        self.f = Figure(figsize=(5,5), dpi=100)
        self.f.set_facecolor('#2c2d37')
        self.a = self.f.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.f, frame)
        self.opening = ''
        self.xList = []
        self.yList = []
        self.labels = []
        self.historic_data = []
        self.current_data = []
        self.today_data = []
        self.labels = []
        self.complete = ''
        while 1:
            try:
                self.get_data(column, command)
                break
            except SyntaxError:
                pass
        self.xy(command, value)
        self.command = eval('self.'+command)
        self.xlabels(self.command)
        self.show(command)
        self.toolbar = NavigationToolbar(self.canvas, frame)
        self.toolbar.config(bg='#2c2d37')
        self.toolbar.update()

class listbox:
    def data(self, y, z, update):
        for i in range(len(z)):
            try:
                listbox_option = str(z[i][0])
            except:
                while 1:
                    pass
            self.listbox_items[i] = Label(self.frame, text=listbox_option, fg = 'white',bg='#2c2d37', height = 2)
            if z[i][1] == 1:
                self.listbox_items[i].config(fg='green')
            if z[i][1] == 0:
                self.listbox_items[i].config(fg='white')
            if z[i][1] == -1:
                self.listbox_items[i].config(fg='red')
            if i != 0:
                self.listbox_spacing[i] = Frame(self.frame, bg='grey')
                self.listbox_spacing[i].pack(fill=X, expand=0)
            self.listbox_items[i].pack(fill=X, expand=1)
            self.listbox_items[i].bind('<Button-1>', (lambda a: lambda event: self.selected(a, y, update))(i))

    def pack(self,):
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(fill=BOTH, expand=True)
        ParentObjects.root.update()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    def pack_forget(self,):
        self.scroll_bar.pack_forget()
        self.canvas.pack_forget()


    def selected(self, i, y, update):
        if self.currently_activated != '':
            self.currently_activated.config(bg='#2c2d37', fg=self.previous_colour)
        self.previous_colour = self.listbox_items[i].cget('fg')
        self.listbox_items[i].config(bg='#2db053', fg='white')
        self.currently_activated = self.listbox_items[i]
        y.set(self.currently_activated.cget('text'))
        update(self.currently_activated.cget('text'), 'today_data')


    def __init__(self, w, x, y, z, update):
        self.scroll_bar = Scrollbar(w)
        self.canvas = Canvas(w, width=x, yscrollcommand=self.scroll_bar.set, bd=0, highlightthickness=0,
                             relief='ridge', bg = '#111111')
        self.scroll_bar.config(command=self.canvas.yview)
        self.frame = Frame(self.canvas)
        self.canvas.create_window(0, 0, width=x, window=self.frame, anchor='n')
        self.currently_activated = ''
        self.listbox_items = {}
        self.listbox_spacing = {}
        self.previous_colour = ''
        self.data(z, y, update)

class purchases_listbox:
    def data(self, a):
        for i in range(len(a)):
            self.outer_selection_frame[i] = Frame(self.frame, bg='#2c2d37')
            self.text_left[i] = Frame(self.outer_selection_frame[i], bg='#2c2d37')
            self.text_right[i] = Frame(self.outer_selection_frame[i], bg='#2c2d37')
            self.sort[i] = Label(self.text_left[i], text=a[i][1], fg='#FFFFFF', bg='#2c2d37')
            self.id[i] = a[i][0]
            self.symbol[i] = Label(self.text_left[i], text=a[i][2], fg='#FFFFFF', bg='#2c2d37',
                                   font="Helvetica 13 bold")
            t1 = 'Investment: £' + a[i][3]
            self.investment[i] = Label(self.text_right[i], text=t1, fg='#FFFFFF', bg='#2c2d37')
            if float(a[i][4])>= 0:
                t2 = 'Profit: £' + a[i][4] + ' (' + a[i][5] + '%)'
                self.profit[i] = Label(self.text_right[i], text=t2, fg='green', bg='#2c2d37')
            else:
                t2 = 'Loss: £' + a[i][4][1:] + ' (' + a[i][5] + '%)'
                self.profit[i] = Label(self.text_right[i], text=t2, fg='red', bg='#2c2d37')


            # self.listbox_items[i] = Label(self.frame, text=listbox_option, fg = '#FFFFFF', bg = '#2c2d37')
            if i != 0:
                self.listbox_spacing[i] = Frame(self.frame, bg='grey')
                self.listbox_spacing[i].pack(fill=X, expand=0)
            self.outer_selection_frame[i].pack(fill=X, expand=1)
            self.text_left[i].pack(side=LEFT, fill = BOTH, expand =1)
            self.text_right[i].pack(side=RIGHT, fill = BOTH, expand = 1)
            self.sort[i].pack(anchor=W)
            self.symbol[i].pack(anchor=W)
            self.investment[i].pack(anchor=E)
            self.profit[i].pack(anchor=E)
            if a[i][6] == 'open':
                self.close[i] = tkButton(self.text_right[i], 'Close', (lambda a: lambda event: self.selected(a))(i),
                                         '#2db053', '#FFFFFF')
                self.close[i].pack(anchor=E, padx=3, pady=3)

    def pack(self):
        #self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(fill=BOTH, expand=True)
        ParentObjects.root.update()

    def selected(self, i):
        data = str(['Purchase.close', str(self.id[i])])
        response = Connection.send(data)
        if response == 'TRUE':
            ParentObjects.purchases_frame.pack_forget()
            PurchasesScreen()
            messagebox.showerror('Success', "Trade has been closed.")
            update_user_data(ParentObjects.user[0])


        else:
            messagebox.showerror('Error', "Trade could not be closed.")
            update_user_data(ParentObjects.user[0])

    def __init__(self, w, x, y):
        self.scroll_bar = Scrollbar(w)
        self.canvas = Canvas(w, width=x, yscrollcommand=self.scroll_bar.set, bd=0, highlightthickness=0, relief='ridge', bg = '#111111')
        self.scroll_bar.config(command=self.canvas.yview)
        self.frame = Frame(self.canvas)
        self.canvas.create_window(250, 0, width=x, window=self.frame, anchor='n')
        self.outer_selection_frame = {}
        self.id = {}
        self.text_left = {}
        self.text_right = {}
        self.sort = {}
        self.symbol = {}
        self.investment = {}
        self.profit = {}
        self.close = {}
        self.listbox_items = {}
        self.listbox_spacing = {}
        self.data(y)



class ConfirmPurchase:
    def display(self, symbol):

        self.f0.pack(fill = BOTH)
        self.f1.pack(fill=X)
        self.f2.pack(fill=BOTH, side=LEFT, expand=1)
        self.f3.pack(fill=BOTH, side=RIGHT, expand=1)
        self.b1.pack(pady = 5)
    def submit(self,type, symbol):
        reset = messagebox.askyesno("Confirm",
                                    "Are you sure you want to continue?")
        if reset == True:
            try:
                float(self.s1.get())
                data = str(['Purchase.trade', ParentObjects.user[0], type, symbol, str(float(self.s1.get()))])
                response = Connection.send(data)
                self.root.destroy()
                if response == 'True':
                    update_user_data(ParentObjects.user[0])

                    messagebox.showerror('Success', "Trade has been completed.")
                else:
                    update_user_data(ParentObjects.user[0])

                    messagebox.showerror('Error', "Trade could not be completed.")
            except ValueError:
                messagebox.showerror('Error', "Amount must be numerical.")
        else:
            update_user_data(ParentObjects.user[0])

            self.root.grab_release()
            self.root.destroy()
    def __init__(self, type, symbol):
        self.root = Tk()
        self.root.grab_set()
        self.root.attributes("-topmost", True)
        self.root.title("Purchase")
        self.root.geometry('300x130')
        c = 20000
        data = str(['GraphData.get_latest', symbol])
        response = eval(Connection.send(data))[0]
        #self.time = response[0][8:10]+':'+response[0][10:12]
        self.rate = response[1]
        self.f0 = Frame(self.root)
        self.f1 = Frame(self.f0)
        self.f2 = Frame(self.f1)
        l1 = Label(self.f2, text='Type:').pack()
        l2 = Label(self.f2, text='Symbol:').pack()
        l3 = Label(self.f2, text='Rate:').pack()
        l5 = Label(self.f2, text='Amount:').pack()
        self.f3 = Frame(self.f1)
        l6 = Label(self.f3, text=type).pack()
        l7 = Label(self.f3, text=symbol).pack()
        l8 = Label(self.f3, text=self.rate).pack()
        self.s1 = Spinbox(self.f3, from_= 40, to=c, width=10, increment=200, format='%10.2f', justify=CENTER)
        self.s1.pack()
        self.b1 = tkButton(self.f0, 'Submit',lambda event: self.submit(type, symbol), '#111111', '#2db053')
        self.display(symbol)
class ChangePassword:
    def update(self):
        if self.passa.get() == self.passb.get() and len(self.passa.get()) > 5:
            data = str(['ChangePassword.update_password', ParentObjects.user[0], self.passwordEntry.get(), self.passa.get()])
            response = Connection.send(data)
            if response == 'FALSE':
                self.backb()
                messagebox.showerror("Error", "Reset failed. Maybe try again later o.O")
            else:
                self.backb()


                messagebox.showerror("Hell Yer!", "Your password has been updated B)")

        else:
            if self.passa.get() != self.passb.get():
                messagebox.showerror("Error", "The passwords you entered doesn't match :|")
            elif len(self.passa.get()) < 6:
                messagebox.showerror("Error", "Your password must be at least 6 characters long :P")
    def check_current(self):
        data = str(['SignIn', ParentObjects.user[0], self.passwordEntry.get()])
        response = Connection.send(data)
        if response == "FALSE":
            messagebox.showerror('Error', "The password you have entered is incorrect.")
        else:
            self.passwordEntry.pack_forget()
            self.b1.pack_forget()
            self.passa.pack(pady=2)
            self.passb.pack(pady=2)
            self.b1.pack(pady=2)
            self.b1.config_text("Update")
            self.b1.config(lambda event: self.update())

    def load(self):
        ParentObjects.father_frame.pack_forget()
        ParentObjects.root.title("Update Password")
        self.l1.pack(pady=2)
        self.l2.pack(pady=2)
        self.passwordEntry.pack(pady=2)
        self.b1.pack(pady=2)
        self.back.pack(pady = 5)
    def backb(self):
        self.back.pack_forget()
        self.f.pack_forget()
        ParentObjects.father_frame.pack(fill = BOTH, expand = 1)
        ParentObjects.root.title("Account - Virtual Trading")
    def __init__(self):

        self.f = Frame(bg = '#2c2d37')
        self.f.pack(expand = 1)
        self.l1 = Label(self.f,text = 'Change Password', font="Helvetica 14 bold ",fg = '#FFFFFF', bg = '#2c2d37')
        self.l2 = Label(self.f,text = ParentObjects.user[0], font="Helvetica 12 italic ",fg = '#FFFFFF', bg = '#2c2d37')
        self.passwordEntry = tkEntry(self.f, 'Current Password', ParentObjects.placeholder_dictionary)
        self.passwordEntry.config(highlightbackground='#111111', bg='#2c2d37')
        self.passa = tkEntry(self.f, 'New Password', ParentObjects.placeholder_dictionary)
        self.passa.config(highlightbackground='#111111', bg='#2c2d37')
        self.passb = tkEntry(self.f, 'Current Password', ParentObjects.placeholder_dictionary)
        self.passb.config(highlightbackground='#111111', bg='#2c2d37')
        self.b1 = tkButton(self.f,'Submit',lambda event: self.check_current(), '#111111', '#2db053')
        self.back = tkButton(ParentObjects.root,'Back',lambda event: self.backb(), '#111111', '#FFFFFF')
class DeleteAccount:
    def load(self):
        ParentObjects.father_frame.pack_forget()
        ParentObjects.root.title("Update Password")
        self.l1.pack(pady=2)
        self.l2.pack(pady=2)
        self.passwordEntry.pack(pady=2)
        self.b1.pack(pady=2)
        self.back.pack(pady=5)
    def check_current(self):
        data = str(['delete_account', ParentObjects.user[0], self.passwordEntry.get()])
        response = Connection.send(data)
        if response == "FALSE":
            messagebox.showerror('Error', "The password you have entered is incorrect.")
        else:
            self.backb()
            move_to_login()
    def backb(self):
        self.back.pack_forget()
        self.f.pack_forget()
        ParentObjects.father_frame.pack(fill=BOTH, expand=1)
        ParentObjects.root.title("Account - Virtual Trading")

    def __init__(self):
        self.f = Frame(bg='#2c2d37')
        self.f.pack(expand=1)
        self.l1 = Label(self.f, text='Delete Account', font="Helvetica 14 bold ", fg='#FFFFFF', bg='#2c2d37')
        self.l2 = Label(self.f, text=ParentObjects.user[0], font="Helvetica 12 italic ", fg='#FFFFFF', bg='#2c2d37')
        self.passwordEntry = tkEntry(self.f, 'Current Password', ParentObjects.placeholder_dictionary)
        self.passwordEntry.config(highlightbackground='#111111', bg='#2c2d37')
        self.b1 = tkButton(self.f, 'Submit', lambda event: self.check_current(), '#111111', '#2db053')
        self.back = tkButton(ParentObjects.root, 'Back', lambda event: self.backb(), '#111111', '#FFFFFF')

class ForexScreen:
    def symbol_list(self):
        Connection.s.send(str(['GraphData.columns', '']).encode())
        data = eval(Connection.s.recv(2048).decode())
        return data
    def load(self):
        ParentObjects.main_contents_frame.pack(side=RIGHT, fill=BOTH, expand=1)
        self.choice_frame.pack(side=LEFT,fill = BOTH,expand = 0)
        self.choice_label_frame.pack(fill = X)
        self.choice_list_frame.pack(fill=BOTH, expand=1)
        self.dropdown_spacer.pack(side = LEFT, fill = Y)
        self.dropdown.pack(fill = BOTH)
        self.symbols_spacer.pack(side = LEFT, fill=Y)
        self.symbols.pack()
        self.selection_information_frame.pack(side=RIGHT, fill = BOTH, expand = 1)
        self.selection_information_title_frame.pack(fill = X)
        self.selection_information_graph_frame.pack(expand = 1, fill = BOTH)
        self.selection_information_graph_label.pack(expand = 1)
        self.selection_information_graph.pack(expand = 1)
        self.selection_information_options_frame.pack(fill = BOTH)
        self.title_label_spacer2.pack(side = LEFT, fill = Y)
        self.title_label.pack(fill=BOTH, expand=1)
        self.title_label_spacer1.pack(fill = X)

    def update_graph(self, column, command):
        self.change_graph_frame.pack_forget()
        #self.change_graph_type.pack_forget()
        self.selection_information_frame.pack_forget()
        self.change_graph_frame.pack(side = TOP, fill = X)
        #self.change_graph_type.pack(side = RIGHT, padx = 70, pady=10)
        self.change_graph_type_year.pack(side = RIGHT, padx = 5, pady=10)
        self.change_graph_type_week.pack(side = RIGHT, padx = 5, pady=10)
        self.change_graph_type_day.pack(side = RIGHT, padx = 5, pady=10)
        self.selection_information_graph.pack_forget()
        self.selection_information_graph= Frame(self.selection_information_graph_frame, bg='#2c2d37')
        self.selection_information_graph.pack(fill = BOTH, expand = 1)
        create_graph(self.selection_information_graph, column, command, self.value)
        self.selection_information_frame.pack(side=RIGHT, fill = BOTH, expand = 1)
        self.selection_information_options_spacer.pack(side = TOP, fill = X)
        self.buy_sell.pack(expand = 1)
        self.buy_sell_top.pack(side = TOP)
        self.buy_sell_bottom.pack()
        self.value_text.pack(side = LEFT)
        self.value.pack(side = RIGHT)
        self.buy_button.pack(side = LEFT, padx = 5)
        self.sell_button.pack(side = RIGHT, padx = 5)
    def change_option(self, value):
        if value == 'Down':
            self.symbols.pack_forget()
            newlist = []
            for i in self.symbol_data:
                if i[1] == -1:
                    newlist.append(i)
            self.symbols = listbox(self.choice_list_frame, 150, newlist, self.current, self.update_graph)
            self.symbols.pack()

        if value == 'Up':
            self.symbols.pack_forget()
            newlist = []
            for i in self.symbol_data:
                if i[1] == 1:
                    newlist.append(i)
            self.symbols = listbox(self.choice_list_frame, 150, newlist, self.current, self.update_graph)
            self.symbols.pack()

        if value == 'All':
            self.symbols.pack_forget()
            self.symbols = listbox(self.choice_list_frame, 150, self.symbol_data, self.current, self.update_graph)
            self.symbols.pack()

    def __init__(self):
        self.choice_frame = Frame(ParentObjects.main_contents_frame , width = '150', bg='#2c2d37')
        self.choice_label_frame = Frame(self.choice_frame, width = '150', height = 40, bg = 'blue')
        self.choice_list_frame = Frame(self.choice_frame, width = '150' ,bg = '#2c2d37')
        #highlightbackground = '#111111', highlightthickness=2,
        self.current = StringVar()

        self.symbols_spacer = Frame(self.choice_list_frame, bg='#111111')

        self.dropdown_selection = StringVar(self.choice_frame)
        self.dropdown_choices = {'All', 'Up', 'Down'}
        self.dropdown_selection.set('All')
        self.dropdown_spacer = Frame(self.choice_label_frame, bg='#111111')
        self.dropdown = OptionMenu(self.choice_label_frame, self.dropdown_selection, *self.dropdown_choices, command=self.change_option)
        self.dropdown.config(bg='#2c2d37', justify='center')

        self.selection_information_frame = Frame(ParentObjects.main_contents_frame, bg='#2c2d37')
        self.selection_information_title_frame = Frame(self.selection_information_frame, bg = 'dark red', height = 40)
        self.title_label = Label(self.selection_information_title_frame, textvariable = self.current, height=1, font="Helvetica 14 bold ", width=15, bg='#2c2d37', fg = 'white')
        self.title_label_spacer1 = Frame(self.selection_information_title_frame, bg='#111111', width=30)
        self.title_label_spacer2 = Frame(self.selection_information_title_frame, bg='#111111')
        self.selection_information_graph_frame = Frame(self.selection_information_frame , bg = '#111111')
        self.change_graph_frame = Frame(self.selection_information_graph_frame, bg = '#2c2d37')
        self.change_graph_type_day = tkButton(self.change_graph_frame, "Today's Data", lambda event: self.update_graph(self.current.get(), 'today_data'), '#2db053', '#FFFFFF')
        self.change_graph_type_week = tkButton(self.change_graph_frame, 'Weekly Data', lambda event: self.update_graph(self.current.get(), 'current_data'), '#2db053', '#FFFFFF')
        self.change_graph_type_year = tkButton(self.change_graph_frame, 'Yearly Data', lambda event: self.update_graph(self.current.get(), 'historic_data'), '#2db053', '#FFFFFF')
        self.selection_information_graph = Frame(self.selection_information_graph_frame, bg = '#111111')
        self.selection_information_graph_label = Label(self.selection_information_graph, text = 'Select a symbol to start.', font="Helvetica 14 bold italic ", bg='#111111', fg = 'white' )
        self.selection_information_options_frame = Frame(self.selection_information_frame , bg = '#2c2d37', height = 150)
        self.selection_information_options_spacer = Frame(self.selection_information_options_frame, bg='#111111')
        self.buy_sell = Frame (self.selection_information_frame , bg = '#2c2d37')
        self.buy_sell_top = Frame(self.buy_sell, bg='#2c2d37')
        self.buy_sell_bottom = Frame(self.buy_sell, bg='#2c2d37')
        self.label_text = 'Value: '+'1234'
        self.value_text = Label(self.buy_sell_top , text = 'Value: ' , font="Helvetica 14 bold", bg='#2c2d37', fg = 'white')
        self.value = Label(self.buy_sell_top , text = '' , font="Helvetica 14 bold", bg='#2c2d37', fg = 'white')

        self.buy_button = tkButton(self.buy_sell_bottom, 'Buy',lambda event:ConfirmPurchase('Buy', self.current.get()), '#2db053', '#FFFFFF')
        self.sell_button = tkButton(self.buy_sell_bottom, 'Sell',lambda event:ConfirmPurchase('Sell',self.current.get()), '#2db053', '#FFFFFF')

        self.symbol_data = self.symbol_list()
        self.symbols = listbox(self.choice_list_frame, 150, self.symbol_data, self.current, self.update_graph)
        self.load()
        ParentObjects.loading_frame.pack_forget()
        ParentObjects.father_frame.pack(fill=BOTH, expand=1)
        ParentObjects.root.title("Forex - Virtual Trading")



class PurchasesScreen:
    def load(self):
        ParentObjects.purchases_frame.pack(side=RIGHT, fill=BOTH, expand=1)
        ParentObjects.root.title("Purchases - Virtual Trading")
        self.frame1.pack(expand = 1,fill = BOTH)
        self.openFrame.pack(side=LEFT, fill=BOTH)
        self.l1.pack(pady = 5)
        self.framet.pack(side=BOTTOM, fill=BOTH, pady = 10, padx = 10, expand = 1)
        self.closedFrame.pack(side=RIGHT, fill=BOTH)
        self.frameq.pack(side=BOTTOM, fill=BOTH,  pady = 10, padx = 10, expand = 1)
        self.l2.pack(pady = 5)

    def __init__(self):
        ParentObjects.purchases_frame = Frame(ParentObjects.father_frame)
        self.frame1 = Frame(ParentObjects.purchases_frame, bg = '#2c2d37')
        self.openFrame = Frame(self.frame1, bg='#2c2d37')
        self.l1 = Label(self.openFrame, text='Open Positions', font="Helvetica 15 bold ", bg='#2c2d37', fg = 'white')
        self.framet = Frame(self.openFrame, bg = '#2c2d37', highlightbackground = '#111111', highlightthickness=2)
        data = str(['Purchase.return_userdata', ParentObjects.user[0], 'open'])
        response = eval(Connection.send(data))
        if response == []:
            self.empty_frame = Frame(self.framet)
            self.empty_frame.pack(expand = 1)
            self.empty_label = Label(self.empty_frame, text='You have no open positions currently.', font="Helvetica 15 bold ", bg='#2c2d37', fg = 'white', width =60)
            self.empty_label.pack()
        else:
            test = purchases_listbox(self.framet, 500, response).pack()
        self.closedFrame = Frame(self.frame1, bg='#2c2d37')
        self.frameq = Frame(self.closedFrame,bg = '#2c2d37', highlightbackground = '#111111', highlightthickness=2)
        self.l2 = Label(self.closedFrame, text='Closed Positions', font="Helvetica 15 bold ", bg='#2c2d37', fg = 'white')
        data2 = str(['Purchase.return_userdata', ParentObjects.user[0], 'closed'])
        response2 = eval(Connection.send(data2))
        if response2 == []:
            self.empty_frame = Frame(self.frameq)
            self.empty_frame.pack(expand = 1)
            self.empty_label = Label(self.empty_frame, text='You have no closed positions currently.', font="Helvetica 15 bold ", bg='#2c2d37', fg = 'white', width =60)
            self.empty_label.pack()
        else:
            test = purchases_listbox(self.frameq, 500, response2).pack()
        self.load()

class AccountScreen:
    def create_change(self):
        x = ChangePassword()
        x.load()
    def create_delete(self):
        x = DeleteAccount()
        x.load()
    def load(self):
        ParentObjects.account_frame.pack(side=RIGHT, fill=BOTH, expand=1)
        ParentObjects.root.title("Account - Virtual Trading")
        self.outer_frame.pack(fill=BOTH, expand=1)
        self.l1.pack(),self.l2.pack(),self.l3.pack(),self.change_password.pack(pady=10),self.l5.pack(),self.l6.pack()
        self.l7.pack(),self.l8.pack(),self.delete_account.pack(pady=10),self.sign_out.pack(pady=10)
        self.parent.pack(expand=1)
        self.logoLabel.pack(pady=20)
        self.logoFrame.pack(expand=1)
        self.testframe.pack(fill=X, expand=1)
        self.detailsFrame.pack(padx=10, pady=20, fill=BOTH, expand=0)


    def __init__(self):
        self.outer_frame = Frame(ParentObjects.account_frame, bg='#2c2d37')
        self.parent = Frame(self.outer_frame, bg='#2c2d37')
        self.detailsFrame = Frame(self.parent, width=200, bg='#2c2d37')
        self.logoFrame = Frame(self.parent, bg='#2c2d37')
        self.l1 = Label(self.detailsFrame, text='Your Details:', font="Helvetica 14 bold ", bg='#2c2d37', fg='white')
        tname = 'Name: '+ParentObjects.user[1]
        self.l2 = Label(self.detailsFrame, text=tname, bg='#2c2d37', fg='white')
        temail = 'Email: '+ParentObjects.user[0]
        self.l3 = Label(self.detailsFrame, text=temail, bg='#2c2d37', fg='white')
        self.l4 = Label(self.detailsFrame, text='Change Password', fg='blue', bg='#2c2d37')
        self.change_password = tkButton(self.detailsFrame, 'Change Password', lambda event:self.create_change(), '#2db053', '#FFFFFF')
        self.l5 = Label(self.detailsFrame, text='Trade Statistics:', font="Helvetica 14 bold ", bg='#2c2d37', fg='white')
        self.l6 = Label(self.detailsFrame, textvariable = ParentObjects.trades , bg='#2c2d37', fg='white')
        self.l7 = Label(self.detailsFrame, textvariable = ParentObjects.average, bg='#2c2d37', fg='white')
        self.l8 = Label(self.detailsFrame, textvariable = ParentObjects.greatest, bg='#2c2d37', fg='white')
        self.sign_out = tkButton(self.detailsFrame, 'Sign Out',lambda event: move_to_login(), '#2db053', '#111111')
        self.b2 = Button(self.detailsFrame, text='Sign Out', bg='#2c2d37', fg='white', highlightbackground='#2c2d37')
        self.delete_account = tkButton(self.detailsFrame, 'Delete Account', lambda event: self.create_delete(), 'red', '#FFFFFF')
        self.l9 = Label(self.detailsFrame, text='Delete Account', fg='red', bg='#2c2d37')
        self.logoLabel = Label(self.logoFrame, image=ParentObjects.about_image, bg='#2c2d37', fg='white')
        self.testframe = Frame(self.parent, bg='white')

        self.load()


class Connection:
    def send(x):
        Connection.s.send(x.encode())
        recieved = Connection.s.recv(1024).decode()
        return recieved
    def start():
        host = '0.0.0.0'
        port = 12383
        Connection.s.connect((host, port))
    def __new__(cls):
        cls.s = socket.socket()

        
if __name__ == '__main__':
    Connection()
    Connection.start()
    root = Tk()
    root.title("Loading Forex - Virtual Trading")
    root.config(bg='#2c2d37')
    ParentObjects(root)
    ParentObjects.user = ['david@dgolding.com','David Golding', 20000, 20000, 0]
    UserInfo(ParentObjects.user)
    MenuBar()
    update_user_data(ParentObjects.user[0])
    ForexScreen()
    root.mainloop()




#2db053
