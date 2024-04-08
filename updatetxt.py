import PySimpleGUI as sg

num = 0

layout = [
    [sg.Text(num, key='xxx')],
    [sg.Button("hi")],
]

window = sg.Window("the box", layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "hi":
        num += 1
        window['xxx'].update(num)

window.close()