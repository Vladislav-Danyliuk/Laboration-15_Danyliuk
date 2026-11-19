import tkinter as tk


path = "C:/Users/danil/Desktop/ICS6/Laboration#15/TEXT.txt"
def sort_words():
    with open (path , "r" , encoding="utf-8") as file:
        words = file.read().split()

    words.sort(key= str.lower)

    
    text.delete("1.0" , tk.END)
    for word in words :
        text.insert(tk.END , word + "\n")

win = tk.Tk()
win.title("Word sorting")
win.geometry("400x400")

fr = tk.Frame(win)
fr.grid(row=0 , column=0)

but = tk.Button(fr , text="Start sorting" , command= sort_words)
but.grid(row= 0 , column= 0)

text = tk.Text(fr , width= 40, height= 20)
text.grid(row= 1 , column= 0)

win.mainloop()