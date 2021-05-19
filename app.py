import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
apps = []
save = 'save.txt'

if os.path.isfile(save):
    with open(save, 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


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


def runapps():
    for app in apps:
        os.startfile(app)


def deleteapps():
    if os.path.exists("save.txt"):
        os.remove("save.txt")
        exit()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addapp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runapps)
runApps.pack()

deleteapps = tk.Button(root, text="Delete Apps", padx=25,
                       pady=10, fg='white', bg="#263D42", command=deleteapps)
deleteapps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open(save, 'w') as f:
    for app in apps:
        f.write(app + ',')
