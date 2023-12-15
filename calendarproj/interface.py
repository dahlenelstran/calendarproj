import tkinter as tk

root = tk.Tk()
root.title('[Control Center] Calendar')

Frame = tk.Frame(root)


mondayFrame = tk.Frame(Frame, width=150, height=800, highlightbackground="black", highlightthickness=1, padx=10)
TuesdayFrame = tk.Frame(Frame, width=150, height=800, highlightbackground="black", highlightthickness=1, padx=10)
WednesdayFrame = tk.Frame(Frame, width=150, height=800, highlightbackground="black", highlightthickness=1, padx=10)
ThursdayFrame = tk.Frame(Frame, width=150, height=800, highlightbackground="black", highlightthickness=1, padx=10)
FridayFrame = tk.Frame(Frame, width=150, height=800, highlightbackground="black", highlightthickness=1, padx=10)

Frame.grid(row=0, column=0)

mondayFrame.grid(row=0, column=0, padx=10)
TuesdayFrame.grid(row=0, column=1, padx=10)
WednesdayFrame.grid(row=0, column=2, padx=10)
ThursdayFrame.grid(row=0, column=3, padx=10)
FridayFrame.grid(row=0, column=4, padx=10)

root.mainloop()
