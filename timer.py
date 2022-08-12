# Timer Progress Bar Windowless application
#
# Getting Started
# 1. Use pip install -r requirements.txt
# 2. python timer.py
from tkinter import ttk
from tkinter import *
from pynput import keyboard
import time
import os
import json

from threading import Thread
import time

with open("config.json", "r") as f:
    config = json.load(f)

# Setup TK sharable variables to get/set state of the timer
root = Tk()
timeLimit = IntVar()
total = IntVar()
run = BooleanVar()
run.set(False)
extra = BooleanVar()
extra.set(False)
timeLimit.set(0)
total.set(80)
label = StringVar()
visible = BooleanVar()
visible.set(True)

# Configure style of the progress bar
# Need to set non default theme so can change progress color as percentage changed
style = ttk.Style(root)
style.theme_use('clam')
# add label in the layout
style.layout('red.Horizontal.TProgressbar', 
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}), 
              ('Horizontal.Progressbar.label', {'sticky': 'nswe'})])
        
# set initial text
style.configure('red.Horizontal.TProgressbar', text=config['defaultText'], anchor='center')
# create progressbar
variable = DoubleVar(root)

# Hide the windows frame
root.overrideredirect(1)

# Position the progress bar
# Make the window only fit the progress bar
leftLocation = int(config["left"])
topLocation = int(config["top"])

root.geometry("200x18+{0}+{1}".format(leftLocation, topLocation))
p = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate",
                    takefocus=True, maximum=100, style='red.Horizontal.TProgressbar')
p['value'] = 0
p.pack()

times = []

with open('times.txt') as f:
    times = f.read().splitlines()

# Use python thread to allow the user to change times via hot keys 
class HotKeysThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        # Setup Hot Keys
        with keyboard.GlobalHotKeys({
                '<ctrl>+<alt>+0': setTime0,
                '<ctrl>+<alt>+1': setTime1,
                '<ctrl>+<alt>+2': setTime2,
                '<ctrl>+<alt>+3': setTime3,
                '<ctrl>+<alt>+4': setTime4,
                '<ctrl>+<alt>+5': setTime5,
                '<ctrl>+<alt>+6': setTime6,
                '<ctrl>+<alt>+7': setTime7,
                '<ctrl>+<alt>+8': setTime8,
                '<ctrl>+<alt>+9': setTime9,
                '<ctrl>+<alt>+h': toggleHide,
                '<ctrl>+<shift>+1': setExtraTime1,
                '<ctrl>+<shift>+2': setExtraTime2,
                '<ctrl>+<shift>+3': setExtraTime3,
                '<ctrl>+<shift>+4': setExtraTime4,
                '<ctrl>+<shift>+5': setExtraTime5}) as h:
            h.join()

    def setTime(val):
        print(val)

# Use python thread to allow the user to enter times via command line interface
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            user_input = input("What do I do ? ")
            print(user_input)

            # User wishes to exit
            if user_input == 'q':
                print('Quitting')
                os._exit(0)
                return

            processKey(user_input)
            
def processKey(val):
    timeLimit.set(0)
    extra.set(False)

    if val.startswith("e"):
        extra.set(True)
        val = val[1:]

    if val.isdigit():
        # Set time progress bar in minutes
        setTime(val)

def clearTime():
    timeLimit.set(0)
    style.configure("red.Horizontal.TProgressbar", text='', foreground='black', background='green')
    run.set(False) 

def toggleHide():
    if visible.get():
        root.withdraw()
        visible.set(False)
    else:
        root.deiconify()
        visible.set(True)

def setTime0():
    processKey('0')

def setTime1():
    processKey(times[0])

def setTime2():
    processKey(times[1])

def setTime3():
    processKey(times[2])

def setTime4():
    processKey(times[3])

def setTime5():
    processKey(times[4])

def setTime6():
    processKey(times[5])

def setTime7():
    processKey(times[6])

def setTime8():
    processKey(times[7])

def setTime9():
    processKey(times[8])


def setExtraTime1():
    processKey('e1')

def setExtraTime2():
    processKey('e2')

def setExtraTime3():
    processKey('e3')

def setExtraTime4():
    processKey('e4')

def setExtraTime5():
    processKey('e5')

# Set a progress bar time in minutes
def setTime(value):
    if value == '0':
        clearTime()
        return

    minutes = int(value)
    total.set(minutes * 60)
    p['value'] = 0
    run.set(True)
    if minutes == 1:
        label.set("1 min")
    else:
        label.set(value + " mins")

def start():
    # Make sure that the window is the top most over top of other windows
    root.lift()   
    root.attributes('-topmost', True)

    warnAtPercentage = int(config['warnAtPercentage'])
    finalAtPercentage = int(config['finalAtPercentage'])

    # Check if running and less than 100% complete
    if p['value'] <= 100 and run.get():
        variable.set(round(timeLimit.get() / total.get() * 100,0))

        extraLabel = ''
        if extra.get():
            extraLabel = config["extraLabel"]
            foregroundColor = config["alternateForeground"]["default"]
            backgroundColor = config["alternateBackground"]["default"]
        else:
            foregroundColor = config["primaryForeground"]["default"]
            backgroundColor = config["primaryBackground"]["default"]

        if p['value'] > warnAtPercentage :
            if extra.get():
                foregroundColor = config["alternateForeground"]["warning"]
                backgroundColor = config["alternateBackground"]["warning"]
            else:
                foregroundColor = config["primaryForeground"]["warning"]
                backgroundColor = config["primaryBackground"]["warning"]

        if p['value'] > finalAtPercentage :
            if extra.get():
                foregroundColor = config["alternateForeground"]["final"]
                backgroundColor = config["alternateBackground"]["final"]
            else:
                foregroundColor = config["primaryForeground"]["final"]
                backgroundColor = config["primaryBackground"]["final"]

        
        style.configure('red.Horizontal.TProgressbar', 
                    text='{0}{1} - {2:g} %'.format(extraLabel, label.get(), variable.get()), foreground=foregroundColor, background=backgroundColor)  # update label
        timeLimit.set(timeLimit.get()+1)
        newValue = (timeLimit.get() / total.get() * 100)
        p['value'] = newValue

    if not run.get():
        # Not running reset
        p['value'] = 0

    # Check again in another second
    root.after(1000, start)

print('Progress Bar')
print('============')
print('Instructions')
print()
print("Press Hot Keys <ctrl>-<alt>-1 to  <ctrl>-<alt>-9 to set default times")
print(times)
print("Press Hot Keys <ctrl>-<shift>-1 to  <ctrl>-<shift>-5 to set extra times")
print(["1","2","3","4","5"])
print()
print("q to quit")
print("Enter number of minutes to countdown in progress")
print("Need to add extra time? Type e<min> to extend by minutes. For example e1 to extend by extra 1 minute")
print()
print('============')

keys = HotKeysThread()

# Open the window
my = MyThread()
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)

root.after(1000, start)
root.mainloop()