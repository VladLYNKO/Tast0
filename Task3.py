import http.client
import json
from tkinter import *
import sys
import os
from tkinter import Tk,Button
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
root = Tk()
root.title("Сovid")
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/europa", headers=headers)
res = conn.getresponse()
data = res.read()
coron = data.decode("utf-8")
json = json.loads(coron)
k="Error"
c1="Italy"
c2="France"
c3="Germany"
c4="Sweden"
c5="Spain"
text = Text(width=500, height=500, fg='#0000FF', bg='#DCDCDC', font=("Times New Roman", 25))
label = Label(text="Назва")
entry = Entry()
label.pack()
entry.pack()
text.pack()
def clicked():
    country = entry.get()
    if country == c1:
        for i in range(1, 2):
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[14])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[12])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[10])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[2])
    elif country == c2:
        for i in range(2, 3):
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[14])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[12])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[10])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[2])
    elif country == c3:
        for i in range(3, 4):
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[14])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[12])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[10])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[2])
    elif country == c4:
        for i in range(4, 5):
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[14])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[12])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[10])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[2])
    elif country == c5:
        for i in range(5, 6):
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[14])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[12])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[10])
            text.insert('1.0', '\n')
            text.insert('1.0', list(json[i].items())[2])
    else:
        text.insert('1.0',k)
Button(root, text="Введення", font=("Times New Roman", 8), command=clicked, fg='#8B0000', bg='#CD5C5C',width=24, height=1,).place(x = 600, y = 55)
Button(root, text="Перезапуск", font=("Times New Roman", 23), command=restart_program, fg='#ffffff', bg='#041f3a',width=40, height=10,).place(x = 690, y = 400)
root.mainloop()