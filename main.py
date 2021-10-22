import tkinter as tk
from tkinter import filedialog, Text
from tkinter.ttk import *
from staticfg import CFGBuilder
from PIL import Image, ImageTk
import os

root =tk.Tk(className=' CFG Builder')
root.geometry("1100x700")
root.configure(bg="#D0E4EC")


#part 1 -----------------------------------------

files=[]
# pyico=tk.PhotoImage(file="python_icon.png")
def addFiles():

    for widget in filesList.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File")
    files.append(filename)
    for file in files:
        # labelLogo=tk.Label(filesList,image=pyico)
        label=tk.Label(filesList,text=file,background="#FFFFFF",font=("Helvetica",15))
        label.pack()
        

frame = tk.Frame(root, bg="#D0DDEC")
frame.place(relwidth=0.3, relheight=1, relx=0.01)

filesList = tk.Frame(root, highlightbackground="#86ABD7",highlightthickness=1.5, bg="#FFFFFF")
filesList.place(relwidth=0.28, relheight=0.5, relx=0.02,rely=0.02)

drop = tk.Frame(root, highlightbackground="#86ABD7",highlightthickness=1.5, bg="#D0DDEC")
drop.place(relwidth=0.28, relheight=0.3, relx=0.02,rely=0.55)

browse=tk.Button(frame,text="BROWSE", padx=35,
pady=5,fg="#000000",bg="#FFFFFF", command=addFiles)
browse.place(relx=0.28,rely=0.9)



#part 2 -----------------------------------------


displayFrame = tk.Frame(root, bg="#D0DDEC", highlightbackground="#86ABD7",highlightthickness=1.5)
displayFrame.place(relwidth=0.67, relheight=0.8, relx=0.31,rely=0.15)

images=[]
def run():
    images.clear()
    for widget in displayFrame.winfo_children():
        widget.destroy()
    for file in files:
        cfg = CFGBuilder().build_from_file('output', file)
        cfg.build_visual('output', 'png',show=False)
        img = Image.open("output.png").resize((650, 450), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        images.append(tkimage)
    

    for tkimages in images:
        label=tk.Label(displayFrame, image=tkimages)
        label.photo=tkimages
        label.pack().pady(5)

def reset():

    for widget in filesList.winfo_children():
        widget.destroy()
    for widget in displayFrame.winfo_children():
        widget.destroy()    
    files.clear()
    images.clear()


buttonsFrame=tk.Frame(root,highlightbackground="#86ABD7",highlightthickness=1.5,bg="#D0E4EC")
buttonsFrame.place(relwidth=0.67, relheight=0.1, relx=0.31,rely=0.02)

bRun=tk.Button(buttonsFrame,text="RUN", padx=60,
pady=10,fg="#FFFFFF",bg="#2DA423", command=run)
bRun.grid(row=0,column=0,padx=(9,0),pady=(7,7))

bSave=tk.Button(buttonsFrame,text="SAVE", padx=60,
pady=10,fg="#FFFFFF",bg="#234FA4", command=addFiles)
bSave.grid(row=0,column=1,padx=(9,0),pady=(7,7))

bDownload=tk.Button(buttonsFrame,text="DOWNLOAD", padx=60,
pady=10,fg="#FFFFFF",bg="#234FA4", command=addFiles)
bDownload.grid(row=0,column=2,padx=(9,0),pady=(7,7))

bReset=tk.Button(buttonsFrame,text="RESET", padx=60,
pady=10,fg="#FFFFFF",bg="#234FA4", command=reset)
bReset.grid(row=0,column=3,padx=(9,0),pady=(7,7))


#part 3 -----------------------------------------


root.mainloop()