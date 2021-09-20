import os
import tkinter as tk
from time import strftime
from tkinter import filedialog, Label, Toplevel

root = tk.Tk()
root.title('App Launcher')
root.iconphoto(False, tk.PhotoImage(file='App-Launcher.png'))
apps = []
save = 'save.txt'

if os.path.isfile(save):
    with open(save, 'r') as f:
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

lbl.pack(anchor='e')
time()


def addapp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        bel = tk.Label(frame, text=app, bg="gray")
        bel.pack()


#def open_win():
 #   global top
  #  top = Toplevel(root)
   # Label(top, text="Manual for operator", font=('Helvetica 14 bold')).pack()
    #canvas = tk.Canvas(top, height=520, width=480, bg="#263D42", cursor='crosshair')
    #canvas.pack(expand=False)

    #frame = tk.Frame(top, bg="white")
    #frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)

   # closeWin = tk.Button(top, text="Close", padx=35, fg='white', bg="#263D42", command=close_newapps)
   # closeWin.pack()
   # top.grab_set()


def runapps():
    for app in apps:
        os.startfile(app)


def close_apps():
    print("Window closed by customer")
    root.destroy()


def deleteapps():
    if os.path.exists("save.txt"):
        os.remove("save.txt")
        exit()


#def close_newapps():
   # print("PopWin closed by customer")
   # top.destroy()


canvas = tk.Canvas(root, height=520, width=480, bg="#263D42", cursor='crosshair')
canvas.pack(expand=False)

frame = tk.Frame(root, bg="white")
frame.place(relx=0.06, rely=0.10, relwidth=0.9, relheight=0.6)

openFile = tk.Button(root, text="Open File", padx=33,
                     pady=10, fg='white', bg="#263D42", command=addapp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=32,
                    pady=10, fg='white', bg="#263D42", command=runapps)
runApps.pack()

#open_window = tk.Button(root, text="New window", padx=23,
                  #      fg='white', bg="#263D42", command=open_win)
#open_window.pack()

deleteapps = tk.Button(root, text="Delete Apps", padx=25,
                       pady=10, fg='white', bg="#263D42", command=deleteapps)
deleteapps.pack()

closeWin = tk.Button(root, text="Close", padx=45,
                     fg='white', bg="#263D42", command=close_apps)
closeWin.pack()
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open(save, 'w') as f:
    for app in apps:
        f.write(app + ',')
