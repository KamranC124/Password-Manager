
def menu():
    MenuOption = int(input("Choose an option: \n 1. View \n 2. Add \n 3. Edit \n 4. Delete \n"))
    print()
    
    Entries = EntryCount()
    if MenuOption == 2:
        AddEntry()
    elif not MenuOption >4:
        ViewEntry(Entries, MenuOption)
    else:
        print("Error")

    MenuOption2 = input("Press enter for further assistance: ")
    if MenuOption2 == "":
        menu()
    else:
        exit()

def EntryCount():
    with open("Manager.txt", "r") as file:
        Entries = (sum(1 for line in file))/4
        return Entries

def ViewEntry(Entries, MenuOption): 
    EntryEnd = (Entries*4)+1
    with open("Manager.txt","r") as file:
        NewFile = file.readlines()
        LineCounter, EntryCounter = 0,0
        for line in NewFile:
            if LineCounter in range (0, int(EntryEnd), 4):
                EntryCounter +=1
                print(f"{EntryCounter}. " + line.strip())
            LineCounter+=1

    MenuOption2 = int(input("Choose an option: "))
    if MenuOption2 > Entries:
        print("Error.")
        pass
    EntryEnd = (MenuOption2*4)+1
    print()
    
    if MenuOption == 1:
        with open("Manager.txt","r") as file:
            NewFile = file.readlines()
            LineCounter = 0
            for line in NewFile:
                LineCounter+=1
                if LineCounter in range (EntryEnd-4,EntryEnd):
                    print(line.strip())
    elif MenuOption == 3:
        EditEntry(EntryEnd)
    elif MenuOption == 4:
        DeleteEntry(EntryEnd)
        
def AddEntry(): 
    Title = input("Title: ")
    Username = input("Username: ")
    Password = input("Password: ")
    with open("Manager.txt", "a") as file:
        file.write(f"{Title} \nUsername: {Username} \nPassword: {Password} \n \n")
        
def EditEntry(EntryEnd): 
    Username = input("Username: ")
    Password = input("Password: ")
    with open("Manager.txt","r+") as file:
        NewFile = file.readlines()
        file.seek(0)
        LineCounter = 0
        for line in NewFile:
            LineCounter+=1
            if LineCounter in range (EntryEnd-3, EntryEnd):
                if LineCounter == EntryEnd-3:
                    file.write(f"Username: {Username} \n")
                elif LineCounter == EntryEnd-2:
                    file.write(f"Password: {Password} \n")
                else:
                    file.write("\n")
            else:
                file.write(line)
        file.truncate()
    
def DeleteEntry(EntryEnd):
    with open("Manager.txt","r+") as file:
        NewFile = file.readlines()
        file.seek(0)
        LineCounter = 0
        for line in NewFile:
            LineCounter+=1
            if LineCounter not in range (EntryEnd-4,EntryEnd):
                file.write(line)
        file.truncate()

menu()

print("End")
