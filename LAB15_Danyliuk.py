import json

eng = ['apple' , 'banana' , 'car' , 'button' , 'computer' , 'laptop' , 'susuge']
ukr = ["яблуко" , "банан" , "автівка" , "кнопка" , "комп'ютер" , "ноутбук" , "сосиска"]

data = {
    'english':eng ,
    "ukrainian":ukr
}
with open ("words.json" , 'w' , encoding="utf-8") as file:
    json.dump(data , file , ensure_ascii=False , indent= 4)
print("JSON-file is on computer now !")

# ------------------------------------------------------------------------------------------ #

import tkinter as tk
win = tk.Tk()
win.title('English - Ukrainian')
win.geometry("630x400")

line = len(eng)
column = 4

for i in range(line):
        fr = tk.Frame(
                    master= win ,
                    relief= tk.RAISED ,
                    borderwidth= 1 ,
                     width=630 , height=400
                )
        fr.grid(row= i // column , column= i % column, padx= 10 , pady= 10)
        L = tk.Label(master= fr , text= f'ENG: {eng[i]} \nUKR: {ukr[i]}' ,
                     foreground='black' , background='skyblue',
                     font= ('Arial' , 12)
                     )
                
        L.pack()

win.mainloop()