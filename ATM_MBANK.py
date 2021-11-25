import sqlite3
from sqlite3.dbapi2 import IntegrityError
from tkinter import *
import tkinter.messagebox

connection = sqlite3.connect('Mbank_Watcharapong.db') 
cur = connection.cursor()

def Exit():
    try:
        exit()
    except:
        exit()

def Back():
    MAINATM()

def back():
    APP_ATM()

def Showmoneytransfer():
    showmoney = Toplevel(background_frame)
    showmoney.title('showmoney')
    height = 70
    width = 200
    screenwidth = showmoney.winfo_screenwidth()
    screenheight = showmoney.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    showmoney.geometry(alignstr)
    showmoney.resizable(False, False)

    #Image
    Image_error = PhotoImage(file='images/moneymaipo.png')
    
    #txt_error
    Label(showmoney, image=Image_error, bg='#54AEFF').pack()
    
    account_entry.delete(0, END)
    money_entry.delete(0, END)

    showmoney.mainloop()

def Showmoneywithdarw():
    showmoney = Toplevel(background_frame)
    showmoney.title('showmoney')
    height = 70
    width = 200
    screenwidth = showmoney.winfo_screenwidth()
    screenheight = showmoney.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    showmoney.geometry(alignstr)
    showmoney.resizable(False, False)

    #Image
    Image_error = PhotoImage(file='images/moneymaipo.png')
    
    #txt_error
    Label(showmoney, image=Image_error, bg='#54AEFF').pack()

    withdraw_entry.delete(0, END)
    
    showmoney.mainloop()

def Slipdeposit():
    slip = Toplevel(background_frame)
    slip.title('Slip')
    height = 450
    width = 800
    screenwidth = slip.winfo_screenwidth()
    screenheight = slip.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    slip.geometry(alignstr)
    slip.resizable(False, False)

    #Image
    Image_slip = PhotoImage(file='images/slipwithdraw.png')
    Image_backapp = PhotoImage(file='images/backapp.png')

    #background
    background_slip = Label(slip, image=Image_slip)
    background_slip.place(relheight=1, relwidth=1)

    #txt
    txt_account = Label(slip, text=Username_login, bg='white', fg='#54AEFF', font='ar 18 bold')
    txt_account.place(x='150', y='91')
    txt_money = Label(slip, text=(money_deposit+'.0 THB') , bg='white', fg='#54AEFF', font='ar 14 bold')
    txt_money.place(x='150', y='188')
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(slip, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='200', y='250')
    
    #BUTTON
    BTN_backapp = Button(slip, image=Image_backapp, bg='#54AEFF', bd=0, activebackground='#54AEFF', command=back)
    BTN_backapp.place(x='125', y='330')

    slip.mainloop()

def Depositcheck():
    #global
    global money_deposit
    money_deposit = data_deposit.get()
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    money_up = connection.execute(Select, [Username_login])
    for d in money_up:
        deposit = d[1] + float(money_deposit)
        money_up.execute('update Mbank set money = ? where Username = ?', (deposit, Username_login))
        connection.commit()
        deposit_entry.delete(0, END)
        Slipdeposit()
        
def Deposit():
    deposit = Toplevel(background_frame)
    deposit.title('Deposit')
    height = 450
    width = 800
    screenwidth = deposit.winfo_screenwidth()
    screenheight = deposit.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    deposit.geometry(alignstr)
    deposit.resizable(False, False)

    #global 
    global data_deposit
    global deposit_entry

    #Val
    data_deposit = StringVar()

    #Image
    Image_deposit = PhotoImage(file='images/backgrounddeposit.png')
    Image_confirm = PhotoImage(file='images/confirm.png')
    Image_back = PhotoImage(file='images/back.png')

    #background
    backgrounddeposit = Label(deposit, image=Image_deposit)
    backgrounddeposit.place(relheight=1, relwidth=1)

    #Entry
    deposit_entry = Entry(deposit, textvariable=data_deposit, bg='white', bd=0, font='ar 18 bold', justify='right')
    deposit_entry.place(x='65', y='230', height='35', width='205')

    #BUTTON
    BTN_confirm = Button(deposit, image=Image_confirm, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Depositcheck)
    BTN_confirm.place(x='107', y='290')
    BTN_back = Button(deposit, image=Image_back, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=back)
    BTN_back.place(x='10')

    #txt
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(deposit, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='172', y='100')
    txt_account = Label(deposit, text=Username_login, bg='white', fg='#54AEFF', font='ar 16 bold')
    txt_account.place(x='145', y='147')

    deposit.mainloop()

def Slipwithdraw():
    slip = Toplevel(background_frame)
    slip.title('Slip')
    height = 450
    width = 800
    screenwidth = slip.winfo_screenwidth()
    screenheight = slip.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    slip.geometry(alignstr)
    slip.resizable(False, False)

    #Image
    Image_slip = PhotoImage(file='images/slipwithdraw.png')
    Image_backapp = PhotoImage(file='images/backapp.png')

    #background
    background_slip = Label(slip, image=Image_slip)
    background_slip.place(relheight=1, relwidth=1)

    #txt
    txt_account = Label(slip, text=Username_login, bg='white', fg='#54AEFF', font='ar 18 bold')
    txt_account.place(x='150', y='91')
    txt_money = Label(slip, text=(money_withdraw+'.0 THB') , bg='white', fg='#54AEFF', font='ar 14 bold')
    txt_money.place(x='150', y='188')
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(slip, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='200', y='250')
    
    #BUTTON
    BTN_backapp = Button(slip, image=Image_backapp, bg='#54AEFF', bd=0, activebackground='#54AEFF', command=back)
    BTN_backapp.place(x='125', y='330')

    slip.mainloop()

def Withdrawcheck():
    #global
    global money_withdraw

    money_withdraw = data_withdraw.get()
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    money_down = connection.execute(Select, [Username_login])
    for w in money_down:
        if w[1] > float(money_withdraw):
            withdraw = w[1] - float(money_withdraw)
            money_down.execute('update Mbank set money = ? where Username = ?', (withdraw, Username_login))
            connection.commit()
            withdraw_entry.delete(0, END)
            Slipwithdraw()
        else:
            Showmoneywithdarw()

def Withdraw():
    withdraw = Toplevel(background_frame)
    withdraw.title('Withdraw')
    height = 450
    width = 800
    screenwidth = withdraw.winfo_screenwidth()
    screenheight = withdraw.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    withdraw.geometry(alignstr)
    withdraw.resizable(False, False)

    #global
    global data_withdraw
    global withdraw_entry

    #Val
    data_withdraw = StringVar()

    #Image
    Image_withdraw = PhotoImage(file='images/backgroundwithdraw.png')
    Image_back = PhotoImage(file='images/back.png')
    Image_confirm = PhotoImage(file='images/confirm.png')

    #background
    backgroundwithdraw = Label(withdraw, image=Image_withdraw)
    backgroundwithdraw.place(relheight=1, relwidth=1)

    #Entry
    withdraw_entry = Entry(withdraw, textvariable=data_withdraw, bg='white', bd=0, font='ar 18 bold', justify='right')
    withdraw_entry.place(x='65', y='230', height='35', width='205')

    #BUTTON
    BTN_confirm = Button(withdraw, image=Image_confirm, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Withdrawcheck)
    BTN_confirm.place(x='110', y='290')
    BTN_back = Button(withdraw, image=Image_back, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=back)
    BTN_back.place(x='10')

    #txt
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(withdraw, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='172', y='100')
    txt_account = Label(withdraw, text=Username_login, bg='white', fg='#54AEFF', font='ar 16 bold')
    txt_account.place(x='145', y='147')
    
    withdraw.mainloop()

def Sliptransfer():
    slip = Toplevel(background_frame)
    slip.title('Slip')
    height = 450
    width = 800
    screenwidth = slip.winfo_screenwidth()
    screenheight = slip.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    slip.geometry(alignstr)
    slip.resizable(False, False)

    #Image
    Image_slip = PhotoImage(file='images/slip.png')
    Image_backapp = PhotoImage(file='images/backapp.png')

    #background
    backgroundslip = Label(slip, image=Image_slip)
    backgroundslip.place(relheight=1, relwidth=1)

    #txt
    txt_Username = Label(slip, text=Username_login, bg='white', fg='#54AEFF', font='ar 18 bold')
    txt_Username.place(x='150', y='91')
    txt_Usernametransfer = Label(slip, text=Usernametransfer, bg='white', fg='#54AEFF', font='ar 18 bold')
    txt_Usernametransfer.place(x='150', y='159')
    txt_money = Label(slip, text=(money_transfer+'.0 THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
    txt_money.place(x='153', y='244')
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(slip, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='214', y='304')
    
    #BUTTON
    BTN_backapp = Button(slip, image=Image_backapp, bg='#54AEFF', bd=0, activebackground='#54AEFF', command=back)
    BTN_backapp.place(x='125', y='344')

    slip.mainloop()

def transfercheck():
    #global
    global money_transfer
    global Usernametransfer

    Usernametransfer = data_account.get()
    money_transfer = data_money.get()
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    money_down = connection.execute(Select, [Username_login])
    money_up = connection.execute(Select, [Usernametransfer])
    for d in money_down:
        if d[1] > float(money_transfer):
            down = d[1] - float(money_transfer)
            money_down.execute('update Mbank set money = ? where Username = ?', (down, Username_login))
            connection.commit()
            for u in money_up:
                up = u[1] + float(money_transfer)
                money_up.execute('update Mbank set money = ? where Username = ?', (up, Usernametransfer))
                connection.commit()
                account_entry.delete(0, END)
                money_entry.delete(0, END)
                Sliptransfer()
        else:
            Showmoneytransfer()
        
def Transfer():
    transfer = Toplevel(background_frame)
    transfer.title('Transfer')
    height = 450
    width = 800
    screenwidth = transfer.winfo_screenwidth()
    screenheight = transfer.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    transfer.geometry(alignstr)
    transfer.resizable(False, False)
    
    #global
    global data_account
    global data_money
    global account_entry
    global money_entry

    #Val
    data_account = StringVar()
    data_money = StringVar()

    #Image
    Image_transfer = PhotoImage(file='images/backgroundtransfer.png')
    Image_confirm = PhotoImage(file='images/confirm.png')
    Image_back = PhotoImage(file='images/back.png')

    #background
    backgroundtransfer = Label(transfer, image=Image_transfer)
    backgroundtransfer.place(relheight=1 ,relwidth=1)
    
    #Entry
    account_entry = Entry(transfer, textvariable=data_account, bg='white', bd=0, font='ar 18 bold')
    account_entry.place(x='77', y='166', height='35', width='242')
    money_entry = Entry(transfer, textvariable=data_money, bg='white', bd=0, font='ar 18 bold',justify='right')
    money_entry.place(x='77', y='238', height='35', width='205')

    #BUTTON
    BTN_confirm = Button(transfer, image=Image_confirm, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=transfercheck)
    BTN_confirm.place(x='120', y='290')
    BTN_back = Button(transfer, image=Image_back, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=back)
    BTN_back.place(x='10')

    #txt
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(transfer, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 12 bold')
        txt_money.place(x='190', y='88')

    transfer.mainloop()

def APP_ATM():
    app = Toplevel(background_frame)
    app.title('APP_ATM')
    height = 450
    width = 800
    screenwidth = app.winfo_screenwidth()
    screenheight = app.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    app.geometry(alignstr)
    app.resizable(False, False)

    #Image
    Image_APP= PhotoImage(file='images/APP.png')
    Image_transfer = PhotoImage(file='images/transfer1.png')
    Image_deposit = PhotoImage(file='images/deposit1.png')
    Image_withdraw = PhotoImage(file='images/withdraw1.png')
    Image_exit = PhotoImage(file='images/exit.png')

    #Background
    background_APP_ATM = Label(app, image=Image_APP)
    background_APP_ATM.place(relheight=1, relwidth=1)
    
    #BUTTON
    BTN_transfer = Button(app, image=Image_transfer, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Transfer)
    BTN_transfer.place(x='45', y='143')
    BTN_deposit = Button(app, image=Image_deposit, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Deposit)
    BTN_deposit.place(x='164', y='143')
    BTN_withdraw = Button(app, image=Image_withdraw, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Withdraw)
    BTN_withdraw.place(x='282', y='143')
    BTN_EXIT = Button(app, image=Image_exit, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Exit)
    BTN_EXIT.place(x='20', y='390')

    #txt
    Select = ('''select Username,money from Mbank
    where Username = ?''')
    account_money = connection.execute(Select, [Username_login])
    for a in account_money:
        txt_money = Label(app, text=(a[1],'THB'), bg='white', fg='#54AEFF', font='ar 18 bold')
        txt_money.place(x='165', y='77')

    app.mainloop()

def logincheck():
    #global
    global Username_login

    Username_login = login_User.get()
    Password_login = login_Pass.get()
    
    Select = ('''
    select Username, Password from Mbank
    where Username = ?''')
    try:
        check = connection.execute(Select, [Username_login])
        for Pass in check:
            if Password_login == Pass[1]:
                User_entry.delete(0, END)
                Pass_entry.delete(0, END)
                APP_ATM()
            else:
                tkinter.messagebox.showinfo('Login','รหัสผ่านไม่ถูกต้อง')
                User_entry.delete(0, END)
                Pass_entry.delete(0, END)
    except EXCEPTION as e:
        print(e)

def ShowPassCon():
    showpasscon = Toplevel(background_frame)
    showpasscon.title('ShowPassCon')
    height = 70
    width = 200
    screenwidth = showpasscon.winfo_screenwidth()
    screenheight = showpasscon.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    showpasscon.geometry(alignstr)
    showpasscon.resizable(False, False)

    #Image
    Image_error = PhotoImage(file='images/PassandCon.png')
    
    #txt_error
    Label(showpasscon, image=Image_error, bg='#54AEFF').pack()

    showpasscon.mainloop()

def Showerror():
    showerror = Toplevel(background_frame)
    showerror.title('Showerror')
    height = 70
    width = 200
    screenwidth = showerror.winfo_screenwidth()
    screenheight = showerror.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    showerror.geometry(alignstr)
    showerror.resizable(False, False)

    #Image
    Image_error = PhotoImage(file='images/error.png')
    
    #txt_error
    Label(showerror, image=Image_error, bg='#54AEFF').pack()

    showerror.mainloop()

def Createtxt():
    Username = data_User.get()
    Password = data_Pass.get()
    Passwordconfirm = data_Con.get()
    
    try:
        if Password == Passwordconfirm:
            cur.execute('INSERT INTO Mbank (Username, Password, Passwordconfirm) values(?, ?, ?)', (Username, Password, Passwordconfirm))
            connection.commit()
            User_entry.delete(0, END)
            Pass_entry.delete(0, END)
            Con_entry.delete(0, END)
            tkinter.messagebox.showinfo('Create', 'สร้างบัญชีใหม่เสร็จสิ้น')
        else:
            ShowPassCon()
    except IntegrityError:
        Showerror()
 
def Create():
    create = Toplevel(background_frame)
    create.title('Create Account')
    height = 450
    width = 800
    screenwidth = create.winfo_screenwidth()
    screenheight = create.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    create.geometry(alignstr)
    create.resizable(False, False)

    #global
    global data_User
    global data_Pass
    global data_Con
    global User_entry
    global Pass_entry
    global Con_entry
    global Image_error
  
    #Val
    data_User = StringVar()
    data_Pass = StringVar()
    data_Con = StringVar()

    #Image
    Image_create = PhotoImage(file='images/backgroundCreate.png')
    Image_Summit = PhotoImage(file='images/Summit.png')
    Image_back = PhotoImage(file='images/back.png')
    
    #Background
    background_create = Label(create, image=Image_create)
    background_create.place(relheight=1, relwidth=1)
    
    #Entry_USER_PASS_CON
    User_entry = Entry(create, textvariable=data_User, bg='white', font='ar 16 bold', bd= 0)
    User_entry.place(x='80', y='123', height='29', width='245')
    Pass_entry = Entry(create, textvariable=data_Pass, bg='white', font='ar 16 bold', bd= 0)
    Pass_entry.place(x='80', y='218', height='29', width='245')
    Con_entry = Entry(create, textvariable=data_Con, bg='white', font='ar 16 bold', bd= 0)
    Con_entry.place(x='80', y='313', height='28', width='245')

    #BUTTON
    BTN_Login = Button(create, image=Image_Summit, bg='#54AEFF',bd=0, activebackground='#54AEFF', command=Createtxt)
    BTN_Login.place(x='125', y='363')
    # BTN_back = Button(create, image=Image_back, bg='#54AEFF', activebackground='#54AEFF', bd=0, command=Back)
    # BTN_back.place(x='10')

    create.mainloop()

def MAINATM():
    Main = Tk()
    Main.title('ATM_BY_WATCHARAPONG')
    height = 450
    width = 800
    screenwidth = Main.winfo_screenwidth()
    screenheight = Main.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    Main.geometry(alignstr)
    Main.resizable(False, False)

    #global
    global background_frame
    global login_User
    global login_Pass
    global User_entry
    global Pass_entry
    global Image_People
    global Image_lock

    #Val
    login_User = StringVar()
    login_Pass = StringVar()

    #Image
    Image_ATM = PhotoImage(file='images/background_ATM.png')
    Image_login = PhotoImage(file='images/login.png')
    Image_People = PhotoImage(file='images/People.png')
    Image_lock = PhotoImage(file='images/lock.png')

    #Background
    background_frame = Label(Main, image=Image_ATM)
    background_frame.place(relheight=1, relwidth=1)
    
    #Entry_USER_PASS
    User_entry = Entry(Main, textvariable=login_User, bg='white', bd=0, font='ar 16 bold')
    User_entry.place(x='80', y='172', height='29', width='245')
    Pass_entry = Entry(Main, textvariable=login_Pass, bg='white', bd=0, font='ar 16 bold', show='*')
    Pass_entry.place(x='80', y='270', height='29', width='245')
    
    #BUTTON
    BTN_Login = Button(Main, image=Image_login, bg='#54AEFF',bd=0, activebackground='#54AEFF', command=logincheck)
    BTN_Login.place(x='130', y='335')
    BTN_Create = Button(Main, text='สร้างบัญชีใหม่?', bg='#54AEFF', fg='white', font='ar 13 bold', bd=0, activebackground='#54AEFF', command=Create)
    BTN_Create.place(x='215', y='300')
    
    Main.mainloop()

MAINATM()