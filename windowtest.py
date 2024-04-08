import PySimpleGUI as sg

words=""
# All the stuff inside your window.
layout = [  [sg.Text("What's your name?")],
            [sg.InputText('')],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Bad Ending')],
            [sg.Text(words, key="txt") ]]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Bad Ending':
        print('Fuck you',values[0], '!')
        words="fuck you!"
        window["txt"].update(words)
    else:
        print('Hello', values[0], '!')

window.close()