import tkinter as tk
from tkinter import simpledialog,filedialog, Text, Listbox
from tkinter.ttk import *
from staticfg import CFGBuilder
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
import fullCover
import os

root =tk.Tk(className=' CFG Builder')
root.geometry("1300x800")
root.configure(bg="#D0E4EC")

#part 1 ---------------------------------------------------------

files=[]
filesHTML=[]
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
filesList.place(relwidth=0.28, relheight=0.4, relx=0.02,rely=0.02)

reportFrame = tk.Frame(root, highlightbackground="#86ABD7",highlightthickness=1.5, bg="#D0DDEC")
reportFrame.place(relwidth=0.28, relheight=0.45, relx=0.02,rely=0.43)

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
def cfgBuilder():
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



bRun=tk.Button(buttonsFrame,text="RUN", padx=70,
pady=15,fg="#FFFFFF",bg="#2DA423", command=cfgBuilder)
bRun.grid(row=0,column=0,padx=(9,0),pady=(7,7))

# bSave=tk.Button(buttonsFrame,text="SAVE", padx=60,
# pady=10,fg="#FFFFFF",bg="#234FA4", command=addFiles)
# bSave.grid(row=0,column=1,padx=(9,0),pady=(7,7))
# bDownload=tk.Button(buttonsFrame,text="DOWNLOAD", padx=60,
# pady=10,fg="#FFFFFF",bg="#234FA4", command=addFiles)
# bDownload.grid(row=0,column=2,padx=(9,0),pady=(7,7))

bReset=tk.Button(buttonsFrame,text="RESET", padx=70,
pady=15,fg="#FFFFFF",bg="#234FA4", command=reset)
bReset.grid(row=0,column=1,padx=(9,0),pady=(7,7))


#part 3 -----------------------------------------

def generateReport():
    tests=entry.get("1.0",'end-1c')
    print(tests)
    
    for file in files:
        filesHTML.append(file.replace(".py",".html").replace("pycodes","htmlcov").replace("htmlcov/","htmlcov/d_6f09c84d57c8bb69_").replace(".html","_py.html"))
        print("python -m coverage run "+file)
        os.system("python -m coverage run "+file+" --lista "+tests)
        os.system("python -m coverage html")
        os.system("python -m coverage report")
        os.system("D:\cfg\htmlcov\index.html")
    print (filesHTML)



disFrame=tk.Frame(reportFrame,bg="#FFFFFF")
disFrame.place(relwidth=0.93, relheight=0.4, relx=0.038,rely=0.045)
entry = tk.Text(disFrame,width=56,height=30,font=("Helvetica", 18),pady=5,padx=5)
entry.pack()

bGenerate=tk.Button(reportFrame,text="Generate report on test case", padx=90,
pady=7,fg="#FFFFFF",bg="#234FA4",command=generateReport)
bGenerate.place(relx=0.038,rely=0.5)



lbFrame=tk.Frame(reportFrame,bg="#FFFFFF")
lbFrame.place(relwidth=0.43, relheight=0.1, relx=0.038,rely=0.63)
lbEntry = tk.Text(lbFrame,width=56,height=20,font=("Helvetica", 14),pady=5,padx=5)
lbEntry.pack()

ubFrame=tk.Frame(reportFrame,bg="#FFFFFF")
ubFrame.place(relwidth=0.43, relheight=0.1, relx=0.538,rely=0.63)
ubEntry = tk.Text(ubFrame,width=56,height=20,font=("Helvetica", 14),pady=5,padx=5)
ubEntry.pack()


def fullCoverageCall():
    lbString = lbEntry.get("1.0",'end-1c')
    ubString = ubEntry.get("1.0",'end-1c')

    if lbString=='' or ubString=='':
        lbString='0'
        ubString='0'

    lbInt = int(lbString)
    ubInt = int(ubString)
    fullCover.fullCoverage(lbInt, ubInt, files)

bCoverage=tk.Button(reportFrame,text="Generate full coverage tests", padx=90,
pady=7,fg="#FFFFFF",bg="#2DA423", command=fullCoverageCall)
bCoverage.place(relx=0.038,rely=0.78)


root.mainloop()