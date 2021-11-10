import tkinter as tk
from tkinter import filedialog, Text, Listbox
from tkinter.ttk import *
from staticfg import CFGBuilder
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
import os

root =tk.Tk(className=' CFG Builder')
root.geometry("1300x800")
root.configure(bg="#D0E4EC")

#part 1 ---------------------------------------------------------

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

reportFrame = tk.Frame(root, highlightbackground="#86ABD7",highlightthickness=1.5, bg="#D0DDEC")
reportFrame.place(relwidth=0.28, relheight=0.35, relx=0.02,rely=0.53)

browse=tk.Button(frame,text="BROWSE", padx=35,
pady=5,fg="#000000",bg="#FFFFFF", command=addFiles)
browse.place(relx=0.28,rely=0.9)



#part 2 -----------------------------------------


xdisplayFrame = tk.Frame(root, bg="#D0DDEC", highlightbackground="#86ABD7",highlightthickness=1.5)
xdisplayFrame.place(relwidth=0.67, relheight=0.8, relx=0.31,rely=0.15)
frame_top = tk.Frame(xdisplayFrame, width=400, height=250)
frame_top.pack(side="top", expand=1, fill="both")

# Create a ScrolledFrame widget
sf = ScrolledFrame(frame_top, width=380, height=240)
sf.pack(side="top", expand=1, fill="both")

# Bind the arrow keys and scroll wheel
sf.bind_arrow_keys(frame_top)
sf.bind_scroll_wheel(frame_top)

displayFrame = sf.display_widget(tk.Frame)

images=[]
def run():
    images.clear()
    for widget in displayFrame.winfo_children():
        widget.destroy()

    for file in files:
        cfg = CFGBuilder().build_from_file('output', file)
        cfg.build_visual('output', 'png',show=False)
        img = Image.open("output.png").resize((850, 650), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        images.append(tkimage)

    for tkimages in images:
        label=tk.Label(displayFrame, image=tkimages)
        label.photo=tkimages
        label.pack()


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

bView=tk.Button(reportFrame,text="View the Report", padx=35,
pady=6,fg="#FFFFFF",bg="#234FA4")
bView.grid(row=0,column=0,padx=(12,4),pady=(170,5))

bGenerate=tk.Button(reportFrame,text="Generate Report", padx=35,
pady=6,fg="#FFFFFF",bg="#2DA423")
bGenerate.grid(row=0,column=1,padx=(8,4),pady=(170,5))

bCoverage=tk.Button(reportFrame,text="Generate full coverage tests", padx=90,
pady=7,fg="#FFFFFF",bg="#234FA4")
bCoverage.place(relx=0.038,rely=0.78)


root.mainloop()