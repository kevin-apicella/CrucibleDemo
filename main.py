import tkinter as tk
import datetime
import customtkinter
from user import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

today = datetime.date.today()
delta = datetime.timedelta(weeks=1)
print(today + delta)
test = "test"
# create window
window = customtkinter.CTk()
window.title('Crucible Demo')
window.geometry("1600x1000")
window.resizable(False, False)

# create user
user = User()

# create gantt chart
fig, gnt = plt.subplots()


def generate_gantt():
    global fig, gnt
    plt.clf()
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 80)
    gnt.set_xlim(0, 200)
    gnt.set_xlabel("Date", color="green", fontsize=24)
    gnt.set_ylabel("tasks", color="green", fontsize=14)
    plt.xticks([20, 34, 48, 62, 76, 90, 104, 118, 132, 146, 160, 174, 188, 202],
               [str(today)[5:], str(today+delta)[5:], str(today+2*delta)[5:], str(today+3*delta)[5:],
                str(today+4*delta)[5:], str(today+5*delta)[5:],str(today+6*delta)[5:], str(today+7*delta)[5:],
                str(today+8*delta)[5:], str(today+9*delta)[5:], str(today+10*delta)[5:], str(today+11*delta)[5:],
                str(today+12*delta)[5:], str(today+13*delta)[5:]])
    plt.yticks([10, 25, 40, 55, 70], ["Fifth", "Fourth", "Third", "Second", "First"])
    gnt.grid(False)
    # first bar
    gnt.broken_barh([(20, 44)], (66, 8), facecolors="tab:orange")
    # second bar
    gnt.broken_barh([(64, 44)], (51, 8))
    # third bar
    gnt.broken_barh([(108, 44)], (36, 8))
    # fourth bar
    gnt.broken_barh([(152, 44)], (21, 8), facecolors="tab:green")
    # fifth bar
    gnt.broken_barh([(196, 10 * int(user.need_embryos))], (6, 8), facecolors="tab:pink")


generate_gantt()

# create widgets
gantt_widget = customtkinter.CTkLabel(window)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
math_widget = customtkinter.CTkLabel(window, text="Math goes here")
lever_widget = customtkinter.CTkLabel(window)

# grid
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# place widgets
gantt_widget.grid(row=0, column=0, sticky="nsew")
math_widget.grid(row=0, column=1, sticky="nsew")
lever_widget.grid(row=1, column=0, columnspan=2, sticky="nsew")

# create levers for lever_widget
selected = tk.StringVar()


# Embryo Question


def embryo_lever():
    global gantt_widget
    global math_widget
    global lever_widget
    global canvas
    user.change_embryo_state(switch_var.get())
    generate_gantt()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    lever_widget = customtkinter.CTkLabel(window)

    print(user.need_embryos)


def switch_event():
    print(switch_var.get())
    switch_var.get()


switch_var = customtkinter.StringVar(value="on")
q1_label = customtkinter.CTkLabel(lever_widget, text="Have you created embryos?")
q1_switch = customtkinter.CTkSwitch(lever_widget, text="CTkSwitch", command=switch_event,
                                    variable=switch_var, onvalue=True, offvalue=False)
q1_commit = customtkinter.CTkButton(lever_widget, text="Commit", command=embryo_lever)
q1_label.grid(row=0, column=0, sticky="nsew")
q1_switch.grid(row=1, column=0, sticky="nsew")
q1_commit.grid(row=3, column=0, sticky="nsew")
# 3)
#

# run the application
window.mainloop()
