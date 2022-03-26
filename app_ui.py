from logging import root
from tkinter.tix import Tk
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tools import convertImageToPdf

class AppUi:
  
    app_root= ''

    def __init__(self) -> Tk:
        pass
        
    def getFileFromLocation(self):
       global im1
       import_file_path = filedialog.askopenfilenames()
       im1 = import_file_path

    def convertToPDF(self) :
       global im1
       export_File_Path = filedialog.asksaveasfilename(defaultextension='.pdf')
       convertImageToPdf('', export_File_Path, im1)


    def exitApplication(self):
       MsBox=messagebox.askquestion('Exit Application', 'Sure to exit ?', icon = 'warning')
       if MsBox == 'yes':
           self.app_root.destroy()

    def Build_UI(self) : 
       self.app_root = tk.Tk()
       bg = 'lightsteelblue2'

       canvas1 = tk.Canvas(self.app_root, width= 300 , height=300, bg= bg, relief= 'raised')
       canvas1.pack()
       
       label1 = tk.Label(self.app_root,text='Image PDF convertion tools', bg=bg )
       label1.config(font=('helvetica', 20))
       canvas1.create_window(150,60, window=label1)
       
       browser_Button = tk.Button(text='Select File ', command=self.getFileFromLocation, bg='green',fg='white', font =('helvetica', 12 , 'bold'))
       canvas1.create_window(150,130, window=browser_Button)
       
       browser_Button = tk.Button(text= 'Convert to PDF', command=self.convertToPDF, bg='green',fg='white', font =('helvetica', 12 , 'bold'))
       canvas1.create_window(150,180, window=browser_Button)
       
       exitBitton = tk.Button(self.app_root,text='Exit', command=self.exitApplication, bg='brown',fg='white', font =('helvetica', 12 , 'bold'))
       canvas1.create_window(150,230, window=exitBitton)
       
       return self.app_root