# dynamically change color
# sidebar on right for creating event (Label) then dragging it, modifying text, resizing to fit certain times
# Frames change size based on window size
# Time labels
# right click functionality on events to delete, edit


import tkinter as tk

# CREATING GENERAL WINDOW

root = tk.Tk()
root.title('[Control Center] Calendar')
root.configure(bg='blue')

# DEFINING FRAMES FOR THE WEEK

WeekFrame = tk.Frame(root)

mondayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
tuesdayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
wednesdayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
thursdayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
fridayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
saturdayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")
sundayFrame = tk.Frame(WeekFrame, width=150, height=800, highlightbackground="#a569bd", highlightthickness=1, bg="#d2b4de")

## defining location on grid

WeekFrame.grid(row=0, column=0)

mondayFrame.grid(row=0, column=0, padx=10, pady=10)
tuesdayFrame.grid(row=0, column=1, padx=10, pady=10)
wednesdayFrame.grid(row=0, column=2, padx=10, pady=10)
thursdayFrame.grid(row=0, column=3, padx=10, pady=10)
fridayFrame.grid(row=0, column=4, padx=10, pady=10)
saturdayFrame.grid(row=0, column=5, padx=10, pady=10)
sundayFrame.grid(row=0, column=6, padx=10, pady=10)

# DEFINING RIGHTMOST FRAME

# DEFINING UPPER FRAME

root.mainloop()
