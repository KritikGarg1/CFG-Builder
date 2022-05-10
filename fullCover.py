from tkinter import *
from tkinter import ttk


import tkinter as tk

from tkinter import simpledialog,filedialog, Text, Listbox
from tkinter.ttk import *
from staticfg import CFGBuilder
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
import os
from bs4 import BeautifulSoup
  
# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))




def fullCoverage(lbEntry,ubEntry,files):
    fullTests=[]
    for i in range(lbEntry,ubEntry+1):    
        fullTests.append(i)
        
    for file in files:
        dictionary={}
        HTMLfile=file.replace(".py",".html").replace("pycodes","htmlcov").replace("htmlcov/","htmlcov/d_6f09c84d57c8bb69_").replace(".html","_py.html")
        for test in fullTests:
            print("python -m coverage run "+file)
            os.system("python -m coverage run "+file+" --lista "+str(test))
            os.system("python -m coverage html")
            os.system("python -m coverage report")
            dictionary[test]=HTMLParser(HTMLfile)
            # os.system("D:\cfg\htmlcov\index.html")
        
        print(dictionary)
        n=len(fullTests);
        min_num_testcases = float('inf')
        actual_testcases = []
        for i in range(1, 2**n):
            x = 1
            y = 0
            missing_lines_curr = []
            testcases = []
            while x <= i:
                if x & i > 0:
                    if len(missing_lines_curr) == 0:
                        missing_lines_curr = dictionary[fullTests[y]]
                        testcases.append(fullTests[y])
                    else:
                        missing_lines_curr = intersection(missing_lines_curr, dictionary[fullTests[y]])
                        testcases.append(fullTests[y])
                x *= 2
                y = y + 1
            if len(missing_lines_curr) == 0:
                if len(testcases) < min_num_testcases:
                    min_num_testcases = len(testcases)
                    actual_testcases = testcases
        

        print(min_num_testcases)
        print(actual_testcases)
        open_popup(file,dictionary,min_num_testcases,actual_testcases)
            


def open_popup(file,dictionary,min_num_testcases,actual_testcases):
   top= Toplevel()
   top.geometry("750x250")
   top.title("Full Coverage Report: "+ file)
   Label(top, text= dictionary, font=('Roboto 14 bold')).place(x=20,y=20)
   Label(top, text= "Minimum size of the set: "+ str(min_num_testcases), font=('Roboto 14')).place(x=20,y=50)
   Label(top, text= "Minimum size set for full coverage: "+str(actual_testcases), font=('Roboto 14')).place(x=20,y=80)

            

def HTMLParser(filePath):
    
    HTMLFile = open(filePath, "r")
    index = HTMLFile.read()
    S = BeautifulSoup(index, 'html.parser')
    
    missing_line_numbers = []

    missing_lines = S.find_all("p", class_= "mis show_mis")
    for line in missing_lines:
        children = line.findChildren();
        for child in children:
            missing_line_numbers.append(int(child.text))
            break
    
    return missing_line_numbers
            

 
