# Noah Gebremariam & Genesis Clarke
# CS330-02

import tkinter as tk

def chooseSeat():
    pass

def createRows():
    seat_counter = 1
    for i in range(20):
        for j in range(1, 7):
            rowButton = tk.Button(win, text='Seat%d' % seat_counter, name='seat%d' % seat_counter)
            rowButton.grid(row = i, column = j)
            seat_counter += 1

def businessYes():
    businessYesLbl = tk.Label(text = "You have chosen business select, please pick a seat in the first or second row")
    businessYesLbl.pack()
    createRows()

def businessNo():
    businessNoLbl = tk.Label(text = "You did not choose business select, chose a row between 3 and 20.")
    businessNoLbl.pack()

def familywithOneChild():
    pass

def familywithTwoChildren():
    pass

def familywithThreeChildren():
    pass

def tourist():
    pass


def family():
    familyLbl = tk.Label(text = "You have chosen family, how many children do you have?")
    onechildbutton = tk.Button(win, text = "One", command = familywithOneChild)
    twochildrenbutton = tk.Button(win, text = "Two", command = familywithTwoChildren)
    threechildrenbutton = tk.Button(win, text = "Three", command = familywithThreeChildren)
    familyLbl.pack()
    onechildbutton.pack()
    twochildrenbutton.pack()
    threechildrenbutton.pack()

def business():
    lbl = tk.Label(text = "You have chosen business, do you want to be seated in business select?")
    button4 = tk.Button(win, text = "Yes", command = businessYes)
    button5 = tk.Button(win, text = "No", command = businessNo)
    lbl.pack()
    button4.pack()
    button5.pack()


win = tk.Tk()
win.geometry("500x500")
win.configure(bg = 'light blue')
button = tk.Button(win, text = "Tourist", command = tourist )
button2 = tk.Button(win, text = "Family", command = family)
button3 = tk.Button(win, text = "Business", command = business)
button.pack()
button2.pack()
button3.pack()
win.mainloop()
