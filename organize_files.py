import os
def file_or_folder(path):
    try:
        os.listdir(path)
        return "folder"
    except:
        return "file"
for i in os.listdir("."):
    if file_or_folder(i) == "file":
        ext = i.split(".")[-1] if "." in i else i
        if ext not in os.listdir("."):
            os.mkdir(ext)
        os.replace(i, os.getcwd()+"\\"+ext+"\\"+i)
    