import shutil
import os

user = input("What is your Mac Username: ")
source_folder = rf"/Users/{user}/"
Desination_folder = rf"/Users/{user}/Library/Mobile Documents/com~apple~CloudDocs/{user}/"
os.chdir(source_folder)

files = os.listdir()

for file in files:
    shutil.copyfile((Desination_folder + file), (source_folder + file))


print("Successuflly uploaded files to iCloud \n"
      "Please do not shut down you immediately computer because \n"
      "It will take some time to upload the folder")