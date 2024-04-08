#!/usr/bin/python3
import PySimpleGUI as sg

liststr="Todo List:\n1. Item 1\n2. Item 2\n3. Item 3"
homelayout=[[sg.Text(liststr, key="liststr")]]

addlayout=[[sg.Text("Adding a new item to list", size=(20,1))],
             [sg.Text("Enter the task name you want to add:", size=(15,1))],
            [sg.InputText('')],
            [sg.Button('Add'), sg.Button('Cancel Add')]]

removeMsg=""
removelayout=[[sg.Text("Remove an item from list", size=(20,1))],
             [sg.Text("Enter the task id you want to remove: ", size=(15,1))],
            [sg.InputText('')],
            [sg.Button('Remove'), sg.Button('Cancel Remove')],
            [sg.Text(removeMsg, key="rmmsg")]]

swapMsg=""
swaplayout=[[sg.Text("Swapping two items from list", size=(20,1))],
             [sg.Text("Please input two list id's: ", size=(15,1))],
            [sg.InputText('')],
            [sg.InputText('')],
            [sg.Button('Swap'), sg.Button('Cancel Swap')],
            [sg.Text(swapMsg, key="swmsg")]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(homelayout, key='homepage'), sg.Column(addlayout, visible=False, key='addpage'), 
           sg.Column(removelayout, visible=False, key='removepage'),sg.Column(swaplayout, visible=False, key='swappage')],
          [sg.Button('add'), sg.Button('remove'), sg.Button('swap'), sg.Button('Exit')]]

window = sg.Window('Todo list', layout)

while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Cancel Add' or event == 'Cancel Remove' or event == 'Cancel Swap':
        window[f'homepage'].update(visible=True)
        window[f'addpage'].update(visible=False)
        window[f'removepage'].update(visible=False)
        window[f'swappage'].update(visible=False)
    elif event == 'add':
        window[f'homepage'].update(visible=False)
        window[f'addpage'].update(visible=True)
        window[f'removepage'].update(visible=False)
        window[f'swappage'].update(visible=False)
    elif event == 'remove':
        window[f'homepage'].update(visible=False)
        window[f'addpage'].update(visible=False)
        window[f'removepage'].update(visible=True)
        window[f'swappage'].update(visible=False)
    elif event == 'swap':
        window[f'homepage'].update(visible=False)
        window[f'addpage'].update(visible=False)
        window[f'removepage'].update(visible=False)
        window[f'swappage'].update(visible=True)
    for i, e in enumerate(values):
        print(f"Index: {i}, Value: {values[i]}")

window.close()