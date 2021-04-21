# Noah Gebremariam & Genesis Clarke
# CS330-02

import tkinter as tk

def saveSeat():
    b.configure(bg = 'red')
    lst = []
    lst.append(b)

def displayRows():
    global b
    new_win = tk.Tk()
    new_win.geometry("500x500")
    new_win.configure(bg = 'light blue')
    seat_counter = 1
    for x in range(20):
        for y in range(1, 7):
            # print('creating seat %d' % seat_counter)
            b = tk.Button(
                new_win, text='Seat%d' % seat_counter,
                name='seat%d' % seat_counter, command = saveSeat
            )
            # doesn't matter that the columns won't line up
            b.grid(row = x, column = y)
            seat_counter += 1

def guestUser():
    win.destroy()
    guestUserWin = tk.Tk()
    guestUserWin.geometry("500x500")
    OptionList = ["Business Select", "Business (Regular)", "Family(1 Child)", "Family(2 Children)", "Family(3 Children)","Tourist",]
    vr = tk.StringVar(guestUserWin)
    vr.set(OptionList[0])
    opt = tk.OptionMenu(guestUserWin, vr, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")
    confirm_btn = tk.Button(guestUserWin, text = "Confirm", command = displayRows)
    confirm_btn.pack()

def admin():
    global w1, w2, e, e1
    win.destroy()
    admin_win = tk.Tk()
    admin_win.title("Admin Login")
    admin_win.geometry("500x500")
    admin_win.configure(bg='light blue')
    w = tk.Label(admin_win, text="LiftServer(Sign-in)")
    w.pack()
    e1 = tk.Label(admin_win, text="******************************")
    e1.pack()
    w1 = tk.Label(admin_win, text="Username")
    w1.pack()
    e = tk.Entry(admin_win)
    e.pack()
    w2 = tk.Label(admin_win, text="Password")
    w2.pack()
    e1 = tk.Entry()
    e1.pack()
    loginButton = tk.Button(admin_win, text="Login", command= validateLogin)
    loginButton.pack()

def validateLogin():
    global errorlbl
    if e.get() == "Noah" and e1.get() == "Password":
        displayRows()
    else:
        errorlbl = tk.Label(text = "Login error")
        errorlbl.pack()
        errorlbl.after(5000, deleteErrorLbl)

def deleteErrorLbl():
    errorlbl.destroy()

win = tk.Tk()
win.geometry("500x500")
win.configure(bg = 'light blue')
introLbl = tk.Label(text = "Are you an administrator or a guest user?")
adminButton = tk.Button(win, text = "Admin", command = admin)
guestUserButton = tk.Button(win, text = "Guest User", command = guestUser)
introLbl.pack()
adminButton.place(x = 150, y = 100)
guestUserButton.place(x = 275, y = 100)
win.mainloop()

