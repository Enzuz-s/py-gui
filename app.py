import os
import tkinter as tk
from time import strftime
from tkinter import filedialog, Label, Toplevel

root = tk.Tk()
root.title('App Launcher')

# Safely load icon
try:
    root.iconphoto(False, tk.PhotoImage(file='App-Launcher.png'))
except tk.TclError:
    print("Icon file 'App-Launcher.png' not found.")

apps = []
save = 'save.txt'

# Safely load saved apps
if os.path.isfile(save):
    with open(save, 'r') as f:
        tempApps = f.read().split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)

# Time display function
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibri', 14, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='e')
time()

# Add application function
def addapp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    if filename:  # Only add if a file was selected
        apps.append(filename)
        print(apps)
        for app in apps:
            bel = tk.Label(frame, text=app, bg="gray")
            bel.pack()

# Run selected applications
def runapps():
    for app in apps:
        try:
            os.startfile(app)
        except Exception as e:
            print(f"Error running {app}: {e}")

# Close the main window
def close_apps():
    print("Window closed by customer")
    root.destroy()

# Delete saved apps file
def deleteapps():
    if os.path.exists(save):
        os.remove(save)
    apps.clear()  # Clear the list in memory
    for widget in frame.winfo_children():
        widget.destroy()

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

deleteapps_btn = tk.Button(root, text="Delete Apps", padx=25,
                           pady=10, fg='white', bg="#263D42", command=deleteapps)
deleteapps_btn.pack()

closeWin = tk.Button(root, text="Close", padx=45,
                     fg='white', bg="#263D42", command=close_apps)
closeWin.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Save the current list of apps to a file on exit
with open(save, 'w') as f:
    f.write(','.join(apps))
