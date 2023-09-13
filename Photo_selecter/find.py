import os
import shutil
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
folder_A = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
print("\nfolder_A : ", folder_A)
folder_B = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
print("\nfolder_B : ", folder_B)
folder_C = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
print("\nfolder_C : ", folder_C)



files_in_A = [os.path.splitext(filename)[0] for filename in os.listdir(folder_A)]

 
for filename in os.listdir(folder_B):
    
    base_filename, _ = os.path.splitext(filename)

    if base_filename in files_in_A:
        source_file = os.path.join(folder_B, filename)
        destination_file = os.path.join(folder_C, filename)

        shutil.copy(source_file, destination_file)
        print(f"file'{filename}'Copy Clear.")

print("Finish")