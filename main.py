import datetime
import customtkinter
from user import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from calc_config import *

# establish date
today = datetime.date.today()
delta = datetime.timedelta(weeks=2)
# create window
window = customtkinter.CTk()
window.title('Crucible Demo')
window.geometry("1200x1000")
window.resizable(False, False)
# create user
user = User()
# create gantt chart
fig, gnt = plt.subplots()


def generate_gantt():
    global fig, gnt
    global user
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 80)
    gnt.set_xlim(0, 200)
    plt.xticks([0, 14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196],
               [str(today)[5:], str(today + delta)[5:], str(today + 2 * delta)[5:], str(today + 3 * delta)[5:],
                str(today + 4 * delta)[5:], str(today + 5 * delta)[5:], str(today + 6 * delta)[5:],
                str(today + 7 * delta)[5:],
                str(today + 8 * delta)[5:], str(today + 9 * delta)[5:], str(today + 10 * delta)[5:],
                str(today + 11 * delta)[5:],
                str(today + 12 * delta)[5:], str(today + 13 * delta)[5:], str(today + 14*delta)[5:]],)
    gnt.tick_params(axis='y', which='major', labelsize=8)
    gnt.tick_params(axis='x', which='major', labelsize=8)
    plt.yticks(options[f"{user.need_eggs}"]["yticks"], options[f"{user.need_eggs}"]["ylabels"], rotation=45)
    for x in range(options[f"{user.need_eggs}"]["length"]):
        gnt.broken_barh([options[f"{user.need_eggs}"]["bars"][x]], (66-15*x, 8),
                        facecolors=f"{options[f'{user.need_eggs}']['colors'][x]}")
    gnt.grid(False)


generate_gantt()

# create widgets
graph_widget = customtkinter.CTkFrame(window, width=800, height=400)
math_widget = customtkinter.CTkFrame(window, width=500, height=1100, fg_color="white", border_color="black",
                                     border_width=2)
lever_widget = customtkinter.CTkFrame(window, width=800, height=600)


# place widgets
graph_widget = customtkinter.CTkFrame(window, width=800, height=400)
graph_widget.place(x=0, y=600)
math_widget.place(x=800, y=0)
lever_widget.place(x=0, y=0)
canvas = FigureCanvasTkAgg(fig, master=graph_widget)
canvas.get_tk_widget().place(x=0, y=-50, width=800, height=450)
# generate text for the button field
questiontext_header = customtkinter.CTkLabel(lever_widget, font=("Arial", 32),
                                text="Are you looking for fresh or frozen donor eggs?")
questiontext_subtext = customtkinter.CTkLabel(lever_widget, font=("Arial", 16), wraplength=550,
                                 text="Fresh eggs mean you get to pick your donor -- and statistically, they are more "
                                      "likely to be successfully fertilized. Frozen eggs save time, and come at a "
                                      "more affordable price point because they've already been retrieved -- you're "
                                      "not paying for an egg donor match.")
questiontext_header.place(x=60, y=100)
questiontext_subtext.place(x=110, y=160)

# generate time calculator text
calctext_header = customtkinter.CTkLabel(math_widget, font=("Arial", 24, "bold"), text_color="black",
                                            text="Your Journey Summary")
calctext_estimated_duration = customtkinter.CTkLabel(math_widget, font=("Arial", 16, "bold"),
                                                     text_color="black", text="ESTIMATED DURATION")
calctext_vendor_selection = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Vendor selection, research")
calctext_vendor_contracting = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Vendor contracting")
calctext_escrow_account_setup = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Escrow account setup")
calctext_ed_matching = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Egg donor matching")
calctext_ed_screening = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Egg donor screening + REI clearance")
calctext_legal_contracting = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Egg donor legal contracting")
calctext_egg_retrieval = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Egg retrieval med cycle")
calctext_embryo_creation = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="blue",
                                            text="Embryo creation")
calctext_embryo_testing = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Embryo testing")
calctext_embryo_freeze = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Embryo freeze")
calctext_surrogate_match = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Surrogate match")
calctext_surrogate_screen = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Surrogate + partner medical screen")
calctext_psych_screen = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Psych screen(IP, partner, Surrogate)")
calctext_surrogate_legal = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Surrogacy legal contracting")
calctext_transfer_med = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Transfer med cycle")
calctext_mock_cycle = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Mock cycle")
calctext_embryo_transfer = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Embryo transfer + test")
calctext_additional_embryo = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Additional embryo transfer")
calctext_pregnancy = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Pregnancy")
calctext_delivery = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                            text="Delivery + Post")
calctext_total_estimated_time = customtkinter.CTkLabel(math_widget, font=("Arial", 14, "bold"), text_color="black",
                                                       text="Total estimated duration")
# generate cost calculator text
calctext_cost_header = customtkinter.CTkLabel(math_widget, font=("Arial", 16, "bold"), text_color="black",
                                               text="COST")
calctext_medical_cost = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Medical cost")
calctext_agency_cost = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Agency cost")
calctext_ed_compensation = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Egg donor compensation")
calctext_surrogate_compensation = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Surrogate compensation")
calctext_surrogate_extras = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Surrogate Extras + Lost Wages")
calctext_surrogate_insurance = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Surrogate insurance")
calctext_legal_fees = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Legal fees")
calctext_escrow_fees = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Escrow management fees")
calctext_newborn_fees = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Newborn fees")
calctext_ip_lost_wages = customtkinter.CTkLabel(math_widget, font=("Arial", 12), text_color="black",
                                               text="Intended parent lost wages")
calctext_total_estimated_cost = customtkinter.CTkLabel(math_widget, font=("Arial", 14, "bold"), text_color="black",
                                                       text="Total estimated cost")


# place time-cost calculator text
def place_timecost_calculator():
    # time calculator text
    calctext_header.place(x=60, y=30)
    calctext_estimated_duration.place(x=60, y=80)
    calctext_vendor_selection.place(x=60, y=105)
    calctext_vendor_contracting.place(x=60, y=130)
    calctext_escrow_account_setup.place(x=60, y=155)
    calctext_ed_matching.place(x=60, y=180)
    calctext_ed_screening.place(x=60, y=205)
    calctext_legal_contracting.place(x=60, y=230)
    calctext_egg_retrieval.place(x=60, y=255)
    calctext_embryo_creation.place(x=60, y=280)
    calctext_embryo_testing.place(x=60, y=305)
    calctext_embryo_freeze.place(x=60, y=330)
    calctext_surrogate_match.place(x=60, y=355)
    calctext_surrogate_screen.place(x=60, y=380)
    calctext_psych_screen.place(x=60, y=405)
    calctext_surrogate_legal.place(x=60, y=430)
    calctext_transfer_med.place(x=60, y=455)
    calctext_mock_cycle.place(x=60, y=480)
    calctext_embryo_transfer.place(x=60, y=505)
    calctext_additional_embryo.place(x=60, y=530)
    calctext_pregnancy.place(x=60, y=555)
    calctext_delivery.place(x=60, y=580)
    calctext_total_estimated_time.place(x=60, y=605)
    # cost calculator text
    calctext_cost_header.place(x=60, y=650)
    calctext_medical_cost.place(x=60, y=675)
    calctext_agency_cost.place(x=60, y=700)
    calctext_ed_compensation.place(x=60, y=725)
    calctext_surrogate_compensation.place(x=60, y=750)
    calctext_surrogate_extras.place(x=60, y=775)
    calctext_surrogate_insurance.place(x=60, y=800)
    calctext_legal_fees.place(x=60, y=825)
    calctext_escrow_fees.place(x=60, y=850)
    calctext_newborn_fees.place(x=60, y=875)
    calctext_ip_lost_wages.place(x=60, y=900)
    calctext_total_estimated_cost.place(x=60, y=925)


place_timecost_calculator()

# generate the calculations for the calculator
time_values_list = [customtkinter.CTkLabel(math_widget, font=("Arial", 14, "bold"), text_color="black",
                                                       text=f"{time_values}w") for time_values in calculations[f"{user.need_eggs}"]["time"]]
x = 1
for entries in time_values_list:
    entries.place(x=340, y=80+(x*25))
    x += 1
cost_values_list = [customtkinter.CTkLabel(math_widget, font=("Arial", 14, "bold"), text_color="black",
                                                       text=f"${cost_values}") for cost_values in calculations[f"{user.need_eggs}"]["cost"]]
z = 1
for entries in cost_values_list:
    entries.place(x=330, y=650+(z*25))
    z += 1


# update calculator values
def update_calculator_values():
    for i, item in enumerate(time_values_list):
        int(item.cget("text").strip("w"))
        if int(item.cget("text").strip("w")) > calculations[f"{user.need_eggs}"]["time"][i]:
            item.configure(text=f"{calculations[f'{user.need_eggs}']['time'][time_values_list.index(item)]}w", text_color="green")
        elif int(item.cget("text").strip("w")) < calculations[f"{user.need_eggs}"]["time"][i]:
            item.configure(text=f"{calculations[f'{user.need_eggs}']['time'][time_values_list.index(item)]}w", text_color="red")
        else:
            item.configure(text=f"{calculations[f'{user.need_eggs}']['time'][time_values_list.index(item)]}w", text_color="black")
    for i, item in enumerate(cost_values_list):
        if int(item.cget("text").strip("$")) > calculations[f"{user.need_eggs}"]["cost"][i]:
            item.configure(text=f"${calculations[f'{user.need_eggs}']['cost'][cost_values_list.index(item)]}", text_color="green")
        elif int(item.cget("text").strip("$")) < calculations[f"{user.need_eggs}"]["cost"][i]:
            item.configure(text=f"${calculations[f'{user.need_eggs}']['cost'][cost_values_list.index(item)]}", text_color="red")
        else:
            item.configure(text=f"${calculations[f'{user.need_eggs}']['cost'][cost_values_list.index(item)]}", text_color="black")


# establish button response commands
def fresh_button_press():
    global canvas
    user.need_eggs = "fresh"
    fresh_button.configure(state="disabled", border_width=1, border_color="white")
    frozen_button.configure(state="standard", border_width=0)
    generate_gantt()
    canvas = FigureCanvasTkAgg(fig, master=graph_widget)
    canvas.get_tk_widget().place(x=0, y=-50, width=800, height=450)
    update_calculator_values()


def frozen_button_press():
    global user
    user.need_eggs = "frozen"
    frozen_button.configure(state="disabled", border_width=1, text="Frozen", border_color="white")
    fresh_button.configure(state="standard", border_width=0)
    generate_gantt()
    canvas = FigureCanvasTkAgg(fig, master=graph_widget)
    canvas.get_tk_widget().place(x=0, y=-50, width=800, height=450)
    update_calculator_values()


# create buttons
fresh_button = customtkinter.CTkButton(master=lever_widget, font=("Arial", 40), text="Fresh", width=200, height=100,
                                       text_color="grey", text_color_disabled="white", command=fresh_button_press)
frozen_button = customtkinter.CTkButton(master=lever_widget, font=("Arial", 40), text="Frozen", width=200, height=100,
                                        text_color="grey", text_color_disabled="white", border_width=1, border_color="white",
                                        state="disabled", command=frozen_button_press)
# commit_button = customtkinter.CTkButton(master=lever_widget, font=("Inter", 40), text="Commit", width=500, height=70)
fresh_button.place(x=130, y=300)
frozen_button.place(x=430, y=300)
# commit_button.place(x=130, y=450)

# run the application
window.mainloop()
