# dynamically change color
# sidebar on right for creating event (Label) then dragging it, modifying text, resizing to fit certain times
# Frames change size based on window size
# Time labels
# right click functionality on events to delete, edit


import tkinter as tk

# CREATING GENERAL WINDOW

root = tk.Tk()
root.title('[Control Center] Calendar')

def do_popup(event):
    try:
        rightClickMenu.tk_popup(event.x_root, event.y_root)
    finally:
        rightClickMenu.grab_release()

# DEFINING FRAMES FOR THE WEEK

WeekFrame = tk.Frame(root)

listOfDayFrames = []

for i in range(7):
    listOfDayFrames.append(tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de"))

for i in listOfDayFrames:
    i.bind("<Button-3>", do_popup)

## defining location on grid

WeekFrame.grid(row=0, column=0)

j = 0

for i in listOfDayFrames:
    i.grid(row=1, column=j, padx=10, pady=5)
    j = j + 1

# DEFINING DAY LABELS + FRAMES
    
labelFrame = tk.Frame(root)

listOfLabelFrames = []

for i in range(7):
    listOfLabelFrames.append(tk.Frame(WeekFrame, width=150, height=50, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de"))

## defining location on grid

labelFrame.grid(row=0, column=0)

j = 0

for i in listOfLabelFrames:
    i.grid(row=0, column=j, padx=10, pady=5)
    j = j + 1

## putting actual text in the boxes
    
labelM = tk.Label(root, text='Monday')
labelM.grid(row=0, column=0)

# DEFINING RIGHT CLICK MENU 

rightClickMenu = tk.Menu(root, tearoff=0)
rightClickMenu.add_command(label="Create Event")
rightClickMenu.add_command(label="Create Task")

# DEFINING RIGHTMOST FRAME

# DEFINING UPPER FRAME

root.mainloop()