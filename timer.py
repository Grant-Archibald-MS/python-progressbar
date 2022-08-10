# Timer Progress Bar Windowless application
#
# Getting Started
# 1. Use pip install -r requirements.txt
# 2. python timer.py
from tkinter import ttk
from tkinter import *
from pynput import keyboard
import time

from threading import Thread
import time

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
style.configure('red.Horizontal.TProgressbar', text='0 %', anchor='center')
# create progressbar
variable = DoubleVar(root)

# Hide the windows frame
root.overrideredirect(1)
# Make the window only fit the progress bar
# TODO: Change to make position configurable
root.geometry("200x18+10+20")
p = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate",
                    takefocus=True, maximum=100, style='red.Horizontal.TProgressbar')
p['value'] = 0
p.pack()

times = []

with open('times.txt') as f:
    times = f.read().splitlines()

# Use python thread to allow the user to 
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
                '<ctrl>+<shift>+1': setExtraTime1,
                '<ctrl>+<shift>+2': setExtraTime2,
                '<ctrl>+<shift>+3': setExtraTime3,
                '<ctrl>+<shift>+4': setExtraTime4,
                '<ctrl>+<shift>+5': setExtraTime5}) as h:
            h.join()

    def setTime(val):
        print(val)

# Use python thread to allow the user to 
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            user_input = input("What do I do (e or minutes) ? ")
            print(user_input)

            # User wishes to exit
            if user_input == 'e':
                sys.exit()

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

    # Check if running and less than 100% complete
    if p['value'] <= 100 and run.get():
        variable.set(round(timeLimit.get() / total.get() * 100,0))

        extraLabel = ''
        if extra.get():
            extraLabel = 'EXTRA '
            foregroundColor = 'black'
            backgroundColor = 'red'
        else:
            foregroundColor = 'black'
            backgroundColor = 'green'

        if p['value'] > 60 :
            if extra.get():
                foregroundColor = 'white'
                backgroundColor = 'brown'
            else:
                backgroundColor = 'orange'

        if p['value'] > 80 :
            if extra.get():
                backgroundColor = 'purple'
            else:
                foregroundColor = 'white'
                backgroundColor = 'red'

        
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
print()
print("Press Hot Keys <ctrl>-<alt>-1 to  <ctrl>-<alt>-9 to set default times")
print(times)
print("Press Hot Keys <ctrl>-<shift>-1 to  <ctrl>-<shift>-5 to set extra times")
print(["1","2","3","4","5"])
print()

keys = HotKeysThread()

# Open the window
my = MyThread()
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)

root.after(1000, start)
root.mainloop()