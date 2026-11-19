import tkinter as tk
win = tk.Tk()
for i in range(3):
    for j in range(3):
        fr = tk.Frame(
            master=win ,
            relief=tk.RAISED,
            borderwidth=1 ,
            width= 100 , height= 100
        )
        fr.grid(row= i , column= j , padx=10 , pady=10)
        lab = tk.Label(master= fr , text= f"Line {i}\nColumn {j}")
        lab.pack()
win.mainloop()