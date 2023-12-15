import tkinter as tk


# creating window

root = tk.Tk()
root.title('[Control Center] Calendar')

# event definition

class Item:
    def __init__(self, day):
        self.day = day

item_class = Item 

# event creation input

entry = tk.Entry(root, width=69)

def day_entry:
    

def event_creation_button():
    day = day_entry.get()
    firstEvent = item_class(day)

# recieving input
    


root.mainloop()
