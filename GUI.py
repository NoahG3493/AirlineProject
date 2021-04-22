import tkinter as tk
import layout
import flight


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                StartPage, AdminPageOne, AdminPageTwo, GuestPageOne, GuestPageTwo, GuestPageTicket, GuestPageAirplane):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# -----------------------------------------------------------------------------------
# START VIEW
# -----------------------------------------------------------------------------------
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to GN Airlines!")
        label.pack(pady=100, padx=200)

        button = tk.Button(self, text="Guest",
                           command=lambda: controller.show_frame(GuestPageOne))
        button.pack()

        button2 = tk.Button(self, text="Admin",
                            command=lambda: controller.show_frame(AdminPageOne))
        button2.pack()


# ---------------------------------------------------------------------------------
# PASSENGER VIEW
# ---------------------------------------------------------------------------------

class GuestPageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome Back!")
        label.pack(pady=10, padx=10)
        w1 = tk.Label(self, text="Enter Flight ID:")
        w1.pack()
        e = tk.Entry(self)
        e.pack()

        button = tk.Button(self, text='View Ticket', command=lambda: controller.show_frame(GuestPageTicket))
        button.pack()

        w1 = tk.Label(self, text="Don't have a seat? No Problem! Click the button below to get started.")

        w1.pack()
        button = tk.Button(self, text='Get Started', fg='green', command=lambda: controller.show_frame(GuestPageTwo))
        button.pack()

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, padx=10)


class GuestPageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What type of traveler are you?")
        label.pack(pady=10, padx=10)

        variable = tk.StringVar(self)
        variable.set("Business Select")  # default value
        w = tk.OptionMenu(self, variable, "Business Select", "Business (Regular)", "Family(1 Child)", "Family(2 "
                                                                                                      "Children)",
                          "Family(3 Children)", "Tourist")
        w.pack()
        label = tk.Label(self, text="By pressing 'Confirm' you acknowledge that you will not be able to change your "
                                    "traveler type until "
                                    "after "
                                    "booking", fg='red')
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Confirm", command=lambda: controller.show_frame(GuestPageAirplane))
        button.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, padx=10)


class GuestPageAirplane(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Airplane Seat Options for: ____")  # fix
        label.pack()

        label2 = tk.Label(self, text="Available Seats = Green\n, Unavailable = Red \n Selected Seat: Yellow")
        label2.pack()
        b = tk.Button(self, text="TEST", bg="white", fg="red",
                      activebackground="blue", activeforeground="black")
        b.pack()

        button = tk.Button(self, text="Confirm", command=lambda: controller.show_frame(GuestPageTicket))
        button.pack(pady=10, padx=10)



class GuestPageTicket(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Flight Ticket:")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, padx=10)


# --------------------------------------------------------------------
# ADMIN VIEW
# --------------------------------------------------------------------

class AdminPageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Admin Login")
        label.pack(pady=10, padx=10)

        # login
        warningLabel = tk.Label(self, text="For administrative work only. If not a administrator, please go back to "
                                           "homepage.", fg="red")
        warningLabel.pack()

        w1 = tk.Label(self, text="Username:")
        w1.pack()
        e = tk.Entry(self)
        e.pack()
        w2 = tk.Label(self, text="Password:")
        w2.pack()
        e1 = tk.Entry(self, show='*')
        e1.pack()

        button2 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame(AdminPageTwo))
        button2.pack()
        button1 = tk.Button(self, text="Back to Homepage",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class AdminPageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Admin Report:")
        label.pack(pady=10, padx=20)
        # example harcoded in; will fix later implementing
        f = flight.Flight("BA758", layout.Layout("Airbus A319",
                                                 20, 6))
        f.allocate_seat('15F', 'Bjarne Stroustrup')
        f.allocate_seat('15E', 'Anders Hejlsberg')
        f.allocate_seat('1C', 'John McCarthy')
        f.allocate_seat('1D', 'Richard Hickey')
        f = f.num_available_seats()
        r = 45
        # creating labels capacity & rating
        reportCap = tk.Label(self, text="Capacity: {}".format(f))
        reportCap.pack()

        reportRating = tk.Label(self, text="Rating: {} / 100".format(r))
        reportRating.pack()

        # back to welcome screen
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

    # button2 = tk.Button(self, text="Page One",
    # command=lambda: controller.show_frame(PageOne))
    # button2.pack()


app = SeaofBTCapp()
app.mainloop()
