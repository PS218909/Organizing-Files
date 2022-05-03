import os
import tkinter as tk
from tkinter import filedialog
def file_or_folder(path):
    try:
        os.listdir(path)
        return "folder"
    except:
        return "file"
def organize(path):
    for i in os.listdir(path):
        if file_or_folder(path+"\\"+i) == "file":
            ext = i.split(".")[-1] if "." in i else i
            if ext not in os.listdir(path):
                os.mkdir(path+"\\"+ext)
            os.replace(path+"\\"+i, path+"\\"+ext+"\\"+i)
    
fd = filedialog.askdirectory().replace("/", "\\")
organize(fd)