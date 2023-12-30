import os
import shutil

print("File System options available:")
print("1. Print Current Directory")
print("2. Change Current Directory")
print("3. Create new folder")
print("4. Create new file")
print("5. Delete all files in current folder")
print("6. Delete a folder")
iterate = True

while iterate == True:
    option = int(input("Enter an option: "))
    if option == 1:
        print("Current Working Directory is:", os.getcwd())
    elif option == 2:
        new_directory = input("Enter the directory name to which it must be changed to: ")
        os.chdir(new_directory)
        print("Current directory has been changed to", new_directory)
    elif option == 3:
        folder_name = input("Enter folder name to be created in current directory: ")
        os.mkdir(folder_name)
        print(f"New folder {folder_name} has been created in the current directory")
    elif option == 4:
        file_name = input("Enter name of the text file to be created:")
        file_contents = input("Enter the contents of the file to be created:")
        myNewFile = open(file_name + ".txt", "a")
        myNewFile.write(file_contents)
        myNewFile.close()
        print(f"New file {file_name + ".txt"} has been created with the entered contents in the current directory.")
    elif option == 5:
        FilesInCurrentFolder = os.listdir(os.getcwd())
        for file in FilesInCurrentFolder:
            os.unlink(file)
            print(f"File {file} has been deleted from the current directory")
    elif option == 6:
        folder_name = input("Enter name of folder to be deleted:")
        FilesInFolder = os.listdir(os.getcwd() + "/" + folder_name)
        if len(FilesInFolder) == 0:
            os.rmdir(folder_name)
            print("Folder has been deleted from the current directory")
        else:
            print("There are some files present in the folder. A folder can only be deleted when it is empty.")
    else:
        iterate = False
