#!/usr/bin/python3
import PySimpleGUI as sg

liststr="Todo list:\n"
tasklist=[]
homelayout=[[sg.Text(liststr, key="liststr")]]

addlayout=[[sg.Text("Adding a new item to list", size=(20,1))],
             [sg.Text("Enter the task name you want to add:", size=(15,1))],
            [sg.InputText('', key="addTxt")],
            [sg.Button('Add'), sg.Button('Cancel Add')]]

removeMsg=""
removelayout=[[sg.Text("Remove an item from list", size=(20,1))],
             [sg.Text("Enter the task id: ", size=(15,1))],
            [sg.InputText('', key="removeTxt")],
            [sg.Button('Remove'), sg.Button('Cancel Remove')],
            [sg.Text(removeMsg, key="rmmsg")]]

swapMsg=""
swaplayout=[[sg.Text("Swapping two items from list", size=(20,1))],
             [sg.Text("Please input two id's: ", size=(15,1))],
            [sg.InputText('', key="swapTxt1")],
            [sg.InputText('', key="swapTxt2")],
            [sg.Button('Swap'), sg.Button('Cancel Swap')],
            [sg.Text(swapMsg, key="swmsg")]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(homelayout, key='homepage'), sg.Column(addlayout, visible=False, key='addpage'), 
           sg.Column(removelayout, visible=False, key='removepage'),sg.Column(swaplayout, visible=False, key='swappage')],
          [sg.Button('add'), sg.Button('remove'), sg.Button('swap'), sg.Button('Exit')]]

window = sg.Window('Todo list', layout)

#helper function to convert task list into a string
def printlist(strlist: list)->str:
    retstr="Todo List:\n"
    for i in range(len(strlist)):
        retstr+=(str(i+1)+". "+strlist[i]+"\n")
    return retstr

#function to help go back to home page
def goBackHome():
    # first update the list string
    newliststr=printlist(tasklist)
    window["liststr"].update(newliststr)

    #then make sure only the homepage is visible
    window[f'homepage'].update(visible=True)
    window[f'addpage'].update(visible=False)
    window[f'removepage'].update(visible=False)
    window[f'swappage'].update(visible=False)

    #update input texts
    #reset the text inputs to blank
    window["addTxt"].update("")
    window["removeTxt"].update("")
    window["swapTxt1"].update("")
    window["swapTxt2"].update("")


#swaps two items in a given list at indices e1 and e2
def swapelem(e1:int, e2:int,strlist: list):
    if e1<0 or e1>=len(strlist) or e2<0 or e2>=len(strlist):
        sg.popup("Requested ID(s) out of bounds")
        return False
    elif e1==e2:
        sg.popup("Can't swap two same IDs")
        return False
    else:
        hold=strlist[e1]
        strlist[e1]=strlist[e2]
        strlist[e2]=hold
        return True

#actually running the window
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Cancel Add' or event == 'Cancel Remove' or event == 'Cancel Swap':
        #if user cancels a process, return back to hompage
        goBackHome()

    #when user goes into the add window
    elif event == 'add':
        # first make sure only the add page is visible
        window[f'homepage'].update(visible=False)
        window[f'addpage'].update(visible=True)
        window[f'removepage'].update(visible=False)
        window[f'swappage'].update(visible=False)

    #when user actually adds an item
    elif event=='Add':
        #add the new task and go back to the home page
        tasklist.append(values["addTxt"])
        goBackHome()
    
    #when user enters remove window
    elif event == 'remove':
        #if there is nothing in the list then don't switch windows
        if len(tasklist)==0:
            sg.popup("List is empty, there is nothing to remove")
        
        else:
            #otherwise switch to the remove window
            window[f'homepage'].update(visible=False)
            window[f'addpage'].update(visible=False)
            window[f'removepage'].update(visible=True)
            window[f'swappage'].update(visible=False)
    
    #when user actually tries to remove an item
    elif event=='Remove':
        target=values["removeTxt"]

        #if user didn't enter an id or if they didn't enter anything
        if not str.isdigit(target):
            sg.popup("Please input a valid number")
        #if the id is out of bounds
        elif int(target)<=0 or int(target)>len(tasklist):
            sg.popup("Please input a number within the bounds of the list")
        #if the number is valid
        else:
            tasklist.pop(int(target)-1)
            goBackHome()
    
    #when user enters swap window
    elif event == 'swap':
        #if there aren't enough element to swap
        if len(tasklist)<2:
            sg.popup("not enough elements to swap")
        #otherwise switch to swap window
        else:
            window[f'homepage'].update(visible=False)
            window[f'addpage'].update(visible=False)
            window[f'removepage'].update(visible=False)
            window[f'swappage'].update(visible=True)
    
    #when user actually tries to swap 2 items
    elif event == "Swap":
        #first get the two targets
        target1=values["swapTxt1"]
        target2=values["swapTxt2"]

        #if the user didn't enter an id or if they didn't enter anything 
        if (not str.isdigit(target1)) or (not str.isdigit(target2)):
            sg.popup("Please input two valid list id's")
        
        #if user inputted two numbers, attempt to swap them
        else:
            success=swapelem(int(target1)-1, int(target2)-1, tasklist)
            #if swapping is succssful, go back to home page
            if success:
                goBackHome()

window.close()