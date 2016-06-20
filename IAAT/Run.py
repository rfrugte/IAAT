# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:42:11 2016

@author: Jordi
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
os.chdir(os.getcwd() + "/program")
import executable
import rd
import clearmaps
os.chdir("..")

TITLE_FONT = ("Helvetica", 28, "bold")
BUTTON_FONT = ("Helvetica", 12, "bold")
TEXT_FONT = ("Helvetica", 12)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Impact Assessment Tool", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)
        number =self.count_pdfs()
        
        label2 = tk.Label(self, text="The PDFs (IAs) must be located in the PDF folder.  ", font=TEXT_FONT)
        label2.pack(side="top", fill="x", pady=0)        

        label4 = tk.Label(self, text=" Press the Continue button if you have converted the PDFs", font=TEXT_FONT)
        label4.pack(side="top", fill="x", pady=0)
        
        label3 = tk.Label(self, text="Number of IAs found: %s" %(number), font=TEXT_FONT)
        label3.pack(side="top", fill="x", pady=0)
        
        button3 = tk.Button(self, text="Clear previous converted files",
                            command=lambda: controller.show_frame("PageSix"), font=BUTTON_FONT, bg="white")
        
        button3.pack()
        button1 = tk.Button(self, text="Convert PDFs",
                            command=lambda: controller.show_frame("PageOne"), font=BUTTON_FONT, bg="white")
        button1.pack()                                      
        button2 = tk.Button(self, text="Continue",
                            command=lambda: controller.show_frame("PageTwo"), font=BUTTON_FONT, bg="white")
        
        button2.pack()
        
    def count_pdfs(self):
        
        number=len(os.listdir(os.path.dirname(os.path.realpath(__file__))+ "/PDF"))
        return number

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Converting", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        #button = tk.Button(self, text="Go to the start page",
                           #command=lambda: controller.show_frame("StartPage"))
        #button.pack()
        
        button2 = tk.Button(self,text="start", command=self.start, font=BUTTON_FONT, bg="white")
        button2.pack()
        self.labels = tk.Label(self, text="", font=TEXT_FONT)
        self.labels.pack(side="top", fill="x", pady=10)
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()
        self.bytes = 0
        self.maxbytes = 0
        self.label2 = tk.Label(self, text="", font=TEXT_FONT)
        self.label2.pack(side="top", fill="x", pady=10)
        self.label3 = tk.Label(self, text="", font=TITLE_FONT)
        self.label3.pack(side="top", fill="x", pady=10)
        
    def start(self):
        self.progress["value"] = 0
        self.maxbytes = len(os.listdir(os.path.dirname(os.path.realpath(__file__))+ "/PDF"))
        self.progress["maximum"] = len(os.listdir(os.path.dirname(os.path.realpath(__file__))+ "/PDF"))
        rd.open_location('/program',False)
        #os.chdir("..")
        #os.chdir(os.getcwd() + "/program")
        import GetFootnotes
        
        GetFootnotes.execute()
        #os.chdir("..")
        rd.open_location('/DOCX',False)
       # os.chdir(os.getcwd() + "/DOCX")
        self.read_bytes()
        os.chdir('..')
    def read_bytes(self):
        if self.bytes < self.maxbytes:
            self.bytes=len(os.listdir(os.path.dirname(os.path.realpath(__file__))+ "/program/DOCX"))
            self.progress["value"] = self.bytes 
            self.label2.config(text="%s/%s"%(self.bytes , self.maxbytes))
            self.after(5000,self.read_bytes)
            
        else:
            self.label3.config(text="Done")
            self.after(1000,self.controller.show_frame("StartPage"))
            
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a method", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        #button = tk.Button(self, text="Go to the start page",
                           #command=lambda: controller.show_frame("StartPage"))
        #button.pack()
        button2 = tk.Button(self,text="Standard execution", command=self.standard, font=BUTTON_FONT, bg="white")
        button2.pack()
        button3 = tk.Button(self,text="+ Hyperlink check", command=self.hyperlink, font=BUTTON_FONT, bg="white")
        button3.pack()
        button4 = tk.Button(self,text="+ Hyperlink check & archive check", command=self.archive, font=BUTTON_FONT, bg="white")
        button4.pack() 
        
        
    def standard(self):
        self.controller.show_frame("PageThree") 

    def hyperlink(self):
        self.controller.show_frame("PageFour")

    def archive(self):
        self.controller.show_frame("PageFive")
        
        
        
        
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Running", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Press start to run the program, an excel file will open when finished", font=TEXT_FONT)
        label2.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self,text="Start", command=self.run, font=BUTTON_FONT, bg="white")
        button2.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"), font=BUTTON_FONT, bg="white")
        button.pack()

    def run(self):        
        executable.run(True,True,True,False,False)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Running", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Press start to run the program, an excel file will open when finished", font=TEXT_FONT)
        label2.pack(side="top", fill="x", pady=10) 
        button2 = tk.Button(self,text="Start", command=self.run, font=BUTTON_FONT, bg="white")
        button2.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"), font=BUTTON_FONT, bg="white")
        button.pack()
    def run(self):                               
        executable.run(True,True,True,True,False)                   

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Running", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Press start to run the program, an excel file will open when finished", font=TEXT_FONT)
        label2.pack(side="top", fill="x", pady=10)   
        button2 = tk.Button(self,text="Start", command=self.run, font=BUTTON_FONT, bg="white")
        button2.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"), font=BUTTON_FONT, bg="white")
        button.pack()
    def run(self):  
        executable.run(True,True,True,True,True)             

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Deleting", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Press start to clear folders", font=TEXT_FONT)
        label2.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self,text="Start", command=self.run, font=BUTTON_FONT, bg="white")
        button2.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"), font=BUTTON_FONT, bg="white")
        button.pack()

    def run(self):        
        clearmaps.execute()    

              
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

