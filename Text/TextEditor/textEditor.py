#Notepad style application that can open, edit, and save text documents
import os


#Menu options
options={"c":"Create New File",
             "e":"Edit Existing File",
             "q":"Exit" }

def print_menu():
    print("Main Menu".center(40,"_"))
    
    for i,j in options.items():
        print(i,j)
    print("Main Menu".center(40,"_"))

def show_files():#this function shows files only in current directory 
    current_dir=os.getcwd()
    print("{}".format(current_dir).center(40,"-"))
    files= os.listdir()
    print(files)
    print("{}".format(current_dir).center(40,"-"))

def create_new_file():

    file_name = input("Enter file_name of a file: ")

    f= open(file_name+".txt","w")

    text = input("Your input: ")
    f.write(text)
    f.close


def read_file(file_name):
    check = os.path.exists(file_name+".txt")

    if check:
        file=open(file_name+".txt","rt")
        print("{}.txt".format(file_name).center(40,'*'))
        print(file.read())
        print("End.txt".center(40,'*'))

    else:
        print("File doesn't exist")

def open_to_edit(file_name):
    check = os.path.exists(file_name+".txt")
    ch=''
    if check:
        while ch !='b':

            options_to_edit={'w':'to overwrite existing file', 'a': 'to add new line','b':'go back main menu ','d':'Delete file'}
            read_file(file_name)
            print("Options".center(40,"*"))
    
            for i,j in options_to_edit.items():
              print(i,j)
            print("***".center(40,'_'))


            ch=input("Your choice : ").lower()
            if ch=='d':
                os.remove(file_name+".txt")
            elif ch!='b':
                f= open(file_name+".txt",ch)

                text = input("Your input: ")+"\n"
                f.write(text)
                f.close
            
    else:
        print("File doesn't exist") 
        
        
#the logic of the app         
choice=''
while choice != '4':
    show_files()
    print_menu()
    choice=input("Please select option : ").lower()
    
    if choice=='c':
            create_new_file()
    elif choice=='e':
            file_name=input("Enter file name: ")
            open_to_edit(file_name)
    elif choice=='q':
            break
        
        
    
