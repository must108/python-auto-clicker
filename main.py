from tkinter import *
from tkinter import ttk
from pynput.mouse import Controller, Button

mouse = Controller()
mouseFlag = False

def simulate_click():
    while not mouseFlag:
        mouse.click(Button.left, 1)

def infiniteClick(event=None):
    global mouseFlag
    mouseFlag = False
    window.after(100, simulate_click)

def stop_click(event=None):
    window.destroy()

# create window and give it a title
window = Tk()
window.title("Python Auto Clicker")
window.iconphoto(True, PhotoImage(file="M:\programs\python\clickauto\mouseimg.png"))
window.bind("<F6>", infiniteClick)
window.bind("<F7>", stop_click)

style = ttk.Style()
style.configure("TRadiobutton")

frame = Frame(window)
frame.pack()

var_repeat = StringVar()
default = 0
default_milli= 100

# create 'click interval' frame
click_interval_frame = LabelFrame(frame, text="Click Interval")
click_interval_frame.grid(row = 0, column = 0, columnspan=2, sticky="ew", padx=(5, 5), pady=(0, 10))

hours_frame = Frame(click_interval_frame)
hours_frame.grid(row = 0, column = 0, padx=10)
minutes_frame = Frame(click_interval_frame)
minutes_frame.grid(row = 0, column = 1, padx=10)
seconds_frame = Frame(click_interval_frame)
seconds_frame.grid(row = 0, column = 2, padx=10)
milli_frame = Frame(click_interval_frame)
milli_frame.grid(row = 0, column = 3, padx=10)

# create input and labels in frame
hours_label = Label(hours_frame, text="hours")
hours_label.grid(row = 0, column = 1)

minutes_label = Label(minutes_frame, text="mins")
minutes_label.grid(row = 0, column = 1)

seconds_label = Label(seconds_frame, text="secs")
seconds_label.grid(row = 0, column = 1)

milli_label = Label(milli_frame, text="milliseconds")
milli_label.grid(row = 0, column = 1)

hours_entry = ttk.Entry(hours_frame, width = 7)
minutes_entry = ttk.Entry(minutes_frame, width = 7)
seconds_entry = ttk.Entry(seconds_frame, width = 7)
milli_entry = ttk.Entry(milli_frame, width = 5)
hours_entry.insert(0, default)
minutes_entry.insert(0, default)
seconds_entry.insert(0, default)
milli_entry.insert(0, default_milli)

hours_entry.grid(row = 0, column = 0)
minutes_entry.grid(row = 0, column = 0)
seconds_entry.grid(row = 0, column = 0)
milli_entry.grid(row = 0, column = 0)

# create 'click options' frame
default_click_options = "Left"
default_type_options = "Single"
click_options_frame = LabelFrame(frame, text="Click Options")
click_options_frame.grid(row = 1, column = 0, sticky="ew", padx=(5, 10))

# input and labels
mouse_button_label = Label(click_options_frame, text="Mouse Button: ")
mouse_combobox = ttk.Combobox(click_options_frame, values = ["Left", "Right", "Middle"], width = 10)
click_type_label = Label(click_options_frame, text="Click Type: ")
click_combobox = ttk.Combobox(click_options_frame, values = ["Single", "Double"], width = 10)
mouse_combobox.set(default_click_options)
click_combobox.set(default_type_options)

mouse_button_label.grid(row = 1, column = 0)
mouse_combobox.grid(row = 1, column = 1)
click_type_label.grid(row = 2, column = 0)
click_combobox.grid(row = 2, column = 1)

# create 'click repeat' frame
click_repeat_frame = LabelFrame(frame, text="Click Repeat")
click_repeat_frame.grid(row = 1, column = 1, sticky="ew", padx=(10, 5))

# input/labels
default_spinbox = 1
default_radio = "repeat_stop"
repeat_radio = ttk.Radiobutton(click_repeat_frame, text="Repeat", variable=var_repeat, value="repeat", style="TRadiobutton")
repeat_radio.grid(row = 0, column = 0, sticky="w")
times_spinbox = ttk.Spinbox(click_repeat_frame, from_=1, to=10, width = 5)
times_spinbox.grid(row = 0, column = 1)
repeat_stop_radio = ttk.Radiobutton(click_repeat_frame, text="Repeat Until Stopped", variable=var_repeat, value="repeat_stop", style="TRadiobutton")
repeat_stop_radio.grid(row = 1, column = 0, sticky="w")
times_spinbox.insert(0, default_spinbox)
var_repeat.set(default_radio)

# buttons
button_frame = Frame(frame)
button_frame.grid(row = 2, column = 0, columnspan= 2, padx = 10, pady = 10)
start_button = ttk.Button(button_frame, text="Start (F6)", command=infiniteClick)
start_button.grid(row = 0, column = 0, ipadx = 10, ipady= 20, padx=(0, 5))
stop_button = ttk.Button(button_frame, text="Stop (F7)", command=window.destroy)
stop_button.grid(row = 0, column = 1, ipadx = 10, ipady= 20, padx=(5, 5))
hotkey_button = ttk.Button(button_frame, text="Hotkey Settings")
hotkey_button.grid(row = 0, column = 2, ipadx = 10, ipady= 20, padx=(5, 0))

# padding 
for widget in click_interval_frame.winfo_children():
    widget.grid_configure(pady = 10)

for widget in click_options_frame.winfo_children():
    widget.grid_configure(padx = 5)
    widget.grid_configure(pady = 6.5)

for widget in click_repeat_frame.winfo_children():
    widget.grid_configure(padx = 7)
    widget.grid_configure(pady = 7.25)

window.geometry('440x240')
window.resizable(False, False)
window.mainloop()

