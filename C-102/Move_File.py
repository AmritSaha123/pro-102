import os
import shutil
from_dir = "/Users/amritsaha/Desktop/C-102"
to_dir = "/Users/amritsaha/Desktop/destination"
listOfFiles = os.listdir(from_dir)
print(listOfFiles)
for f in listOfFiles:
    name,ext = os.path.splitext(f)
    print(name)
    print(ext)
    if ext =="":
        continue
    if ext in ['.txt','.pdf','.doc','.docx']:
        path1 = from_dir+"/"+f
        path2 = to_dir+"/"+"document_files"
        path3 = to_dir+"/"+"document_files"+"/"+f
        if os.path.exists(path2):
            print("moving "+f)
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print("moving "+f)
            shutil.move(path1,path3)