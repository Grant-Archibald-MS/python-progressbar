# Timer Progress Bar Windowless application
#
# Getting Started
# 1. Use pip install -r requirements.txt
# 2. python timer.py
from tkinter import ttk
from tkinter import *
import time

from threading import Thread
import time

root = Tk()
timeLimit = IntVar()
total = IntVar()
run = BooleanVar()
run.set(False)
extra = BooleanVar()
run.set(False)
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

# Use python thread to allow the user to 
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            user_input = input("What do I do ? ")
            print(user_input)

            # User wishes to exit
            if user_input == 'e':
                sys.exit()


            timeLimit.set(0)
            extra.set(False)

            if user_input.startswith("e"):
                extra.set(True)
                user_input = user_input[1:]


            if user_input == '0':
                # User wants to pause timer and reset
                style.configure("red.Horizontal.TProgressbar", foreground='black', background='green')
                run.set(False)

            # Set time progress bar in minutes (1-10)
            if user_input == '1':
                total.set(60)
                p['value'] = 0
                run.set(True)
                label.set("1 min")

            if user_input == '2':
                total.set(120)
                p['value'] = 0
                run.set(True)
                label.set("2 mins")

            if user_input == '3':
                total.set(180)
                p['value'] = 0
                run.set(True)
                label.set("3 mins")

            if user_input == '4':
                total.set(240)
                p['value'] = 0
                run.set(True)
                label.set("4 mins")

            if user_input == '5':
                total.set(300)
                p['value'] = 0
                run.set(True)
                label.set("5 mins")

            if user_input == '6':
                total.set(360)
                p['value'] = 0
                run.set(True)
                label.set("6 mins")

            if user_input == '10':
                total.set(600)
                p['value'] = 0
                run.set(True)
                label.set("10 mins")


def start():
    # Make sure that the window is the top most over top of other windows
    root.lift()   
    root.attributes('-topmost', True)

    # Check if running and less than 100% complete
    if p['value'] <= 100 and run.get():
        variable.set(round(timeLimit.get() / total.get() * 100,0))
        foregroundColor = 'black'
        backgroundColor = 'green'

        if p['value'] > 60 :
            backgroundColor = 'orange'

        if p['value'] > 80 :
            foregroundColor = 'white'
            backgroundColor = 'red'

        extraLabel = ''
        if extra.get():
            extraLabel = 'EXTRA '

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

# Open the window
my = MyThread()
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)

root.after(1000, start)
root.mainloop()