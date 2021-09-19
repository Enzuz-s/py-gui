import os
import tkinter as tk
from time import strftime
from tkinter import filedialog, Label, Toplevel

root = tk.Tk()
root.title('beta version')
apps = []
top = Toplevel(root)

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 14, 'bold'),
            background='black',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='e')
time()


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def open_win():
    global top
    Label(top, text="Manual for operator", font='Helvetica 14 bold').pack()
    canvas = tk.Canvas(top, height=520, width=480, bg="#263D42", cursor='crosshair')
    canvas.pack(expand=False)

    frame = tk.Frame(top, bg="white")
    frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)

    closeWin = tk.Button(top, text="Close", padx=35, fg='white', bg="#263D42", command=close_newapps)
    closeWin.pack()
    top.grab_set()


def runApps():
    for app in apps:
        os.startfile(app)


def deleteapps():
    if os.path.exists("save.txt"):
        os.remove("save.txt")
        exit()


def close_apps():
    print("Window closed by customer")
    root.destroy()


def close_newapps():
    print("PopWin closed by customer")
    top.destroy()


canvas = tk.Canvas(root, height=520, width=480, bg="#263D42", cursor='crosshair')
canvas.pack(expand=False)

frame = tk.Frame(root, bg="white")
frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)

openFile = tk.Button(root, text="Open File", padx=25, fg='white', bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=25, fg='white', bg="#263D42", command=runApps)
runApps.pack()

deleteapps = tk.Button(root, text="Delete Apps", padx=25,
                       pady=10, fg='white', bg="#263D42", command=deleteapps)
deleteapps.pack()
open_window = tk.Button(root, text="New window", padx=35, fg='white', bg="#263D42", command=open_win)
open_window.pack()

closeWin = tk.Button(root, text="Close", padx=35, fg='white', bg="#263D42", command=close_apps)
closeWin.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
