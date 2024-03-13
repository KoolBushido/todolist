#!/usr/bin/python3
"""
prints out a list starting at 1
"""
def printlist(strlist: list):
    if len(strlist)>0:
        print("Tasklist:")
    for i in range(len(strlist)):
        print(str(i+1)+". "+strlist[i])

"""
prints out the commands that the program takes
"""
def printcommands():
    print("[q-quit, a-add to list, r-remove from list, s-swap list items]")

"""
swaps two items in a given list at indices e1 and e2
"""
def swapelem(e1:int, e2:int,strlist: list)->bool:
    if e1<0 or e1>=len(strlist) or e2<0 or e2>=len(strlist):
        print("Requested ID(s) out of bounds")
        return False
    elif e1==e2:
        print("Can't swap two same IDs")
        return False
    else:
        hold=strlist[e1]
        strlist[e1]=strlist[e2]
        strlist[e2]=hold
        return True

"""
check that all elements in a list are integers
"""
def checkListIsInt(alist: list)->bool:
    for x in alist:
        if not str.isdigit(x):
            return False
    return True

run = True
tasklist=[]
print("Welcome to the A-list! This program will help you keep track of your tasks!")

while run:
    #first print out the list and the available commands
    print()
    printlist(tasklist)
    print()
    printcommands()

    #Then take in a command
    command=input("Enter your command: ")
    
    #when user wants to quit
    if command=="q":
        print("Thank you for using the A-list")
        run=False
    #when user wants to add a new item
    elif command=="a":
        command=input("Enter the task name you want to add: ")
        tasklist+=[command]
    #when user wants to remove an item from list
    elif command=="r":
        #if the list is empty remove can't be ran
        if len(tasklist)==0:
            print("List is empty, there is nothing to remove")
        #if list isn't empty, ask for the item number
        else:
            command=input("Enter the task id you want to remove or c to cancel: ")
            remove=True
            
            #runs until remove is canceled or a succeeded
            while remove:
                #if user was prompted to enter another number but decided to cancel instead
                if command=="c":
                    print("remove canceled")
                    remove=False
                elif not str.isdigit(command):
                    command=input("please input a valid number or c to cancel: ")
                #if the number is out of bounds then request another number
                elif int(command)<=0 or int(command)>len(tasklist):
                    command=input("please input a number within the bounds of the list or c to cancel: ")
                #if the number is valid
                else:
                    print("item "+command+" was removed successfully")
                    tasklist.pop(int(command)-1)
                    remove=False
    #when the user wants to swap items
    elif command=="s":
        #if the list has less than 2 items, nothing can be swapped
        if len(tasklist)<2:
            print("not enough elements to swap")
        #if the lenght of the list is at least 2
        else:
            ids=input("Please input two list id's separated by space or c to cancel:\n")
            ids=ids.split()
            swap=True
            #runs until swap is canceled or succeeded
            while swap:
                #if the swap was canceled
                if ids[0]=="c":
                    print("Swap canceled")
                    swap=False
                #if the input wasn't all ints or user inputted more than two entries
                elif not checkListIsInt(ids) or len(ids)!=2:
                    ids=input("Please input two valid list id's or c to cancel:\n")
                    ids=ids.split()
                #if user inputted two numbers, attempt to swap them
                else:
                    success=swapelem(int(ids[0])-1, int(ids[1])-1, tasklist)
                    #if the swap was successful
                    if success:
                        print("Swap successful")
                        swap=False
                    #if the swap wasn't successful, inform the user and request another input
                    else:
                        ids=input("Please input two valid list id's or c to cancel:\n")
                        ids=ids.split()
    else:
        print("please input a valid command")
            