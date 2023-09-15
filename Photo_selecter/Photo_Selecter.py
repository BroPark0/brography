import os
import shutil
import tkinter
from tkinter import *
from tkinter import filedialog


# root.withdraw()

def Select():
    global folder_A
    folder_A = filedialog.askdirectory(parent=root,initialdir="/",title='Select a folder')
    print("\nfolder_A : ", folder_A)
    if folder_A:
        folder_A_label.config(text=folder_A)

def Raw():
    global folder_B
    folder_B = filedialog.askdirectory(parent=root,initialdir="/",title='Raw folder')
    print("\nfolder_B : ", folder_B)
    if folder_B:
        folder_B_label.config(text=folder_B)


def Save():
    global folder_C
    folder_C = filedialog.askdirectory(parent=root,initialdir="/",title='Save a folder')
    print("\nfolder_C : ", folder_C)
    if folder_C:
        folder_C_label.config(text=folder_C)



def Start():
    files_in_A = [os.path.splitext(filename)[0] for filename in os.listdir(folder_A)]

    for filename in os.listdir(folder_B):
        
        base_filename, _ = os.path.splitext(filename)

        if base_filename in files_in_A:
            source_file = os.path.join(folder_B, filename)
            destination_file = os.path.join(folder_C, filename)

            shutil.copy(source_file, destination_file)
            print(f"file'{filename}'Copy Clear.")

    print("Finish")
    if Finish:
        Finish_label.config(text="Finish")


def Finish():
    root.destroy()

root = tkinter.Tk()
root.title("made by Bro")
# 생성할 window 창의 크기 및 초기 위치 설정 매서드: geometry()
window_width = 400
window_height = 150
window_pos_x = 700
window_pos_y = 100




root.geometry("{}x{}+{}+{}".format(window_width, window_height, window_pos_x, window_pos_y))

root.resizable(False, False)    #가로 *세로 사이즈 변경 가능 유무
folder_A_label = Label(root, text="",  width = 42)
folder_A_label.grid(row=1, column=1)

button1 = tkinter.Button(root, text="Select", command=Select, width = 10)
button1.grid(row=1, column=2)


folder_B_label = Label(root, text="",  width = 42)
folder_B_label.grid(row=2, column=1)
button2 = tkinter.Button(root, text="Raw", command=Raw,  width = 10)
button2.grid(row=2, column=2)

folder_C_label = Label(root, text="",  width = 42)
folder_C_label.grid(row=3, column=1)

button3 = tkinter.Button(root, text="Save", command=Save, width = 10)
button3.grid(row=3, column=2)

Finish_label = Label(root, text="",  width = 42)
Finish_label.grid(row=4, column=1)

button4 = tkinter.Button(root, text="Start", command=Start,  width = 10)
button4.grid(row=4, column=2)

button4 = tkinter.Button(root, text="Finish", command=Finish,  width = 10)
button4.grid(row=5, column=2)



root.mainloop()