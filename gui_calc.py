import PySimpleGUI as sg

# All the stuff inside your window.
x = y = None
adding = subtracting = multiplying = dividing = False
textBox = sg.InputText(size=(15,10), disabled=True)
layout = [
            [textBox],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
            [sg.Button('0'), sg.Button('/'), sg.Button('=')],
            [sg.Button('Clear'), sg.Button('Exit')] 
        ]

# Functions
def clearValue(element):
    element.update(value='')

def concatTextWindow(text, newValue):
    currText = text.get()
    text.update(value=(currText + newValue))

def numberPressed(event):
    return (
        event == '1' or
        event == '2' or
        event == '3' or
        event == '4' or
        event == '5' or
        event == '6' or
        event == '7' or
        event == '8' or
        event == '9' or
        event == '0'
    )

# Create the Window
window = sg.Window('Window Title', layout, finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break

    elif event == 'Clear':
        clearValue(textBox)

    elif numberPressed(event):
        concatTextWindow(textBox, event)

    elif event == '+':
        x = int(textBox.get())
        clearValue(textBox)
        adding = True
    
    elif event == '-':
        x = int(textBox.get())
        clearValue(textBox)
        subtracting = True

    elif event == '*':
        x = int(textBox.get())
        clearValue(textBox)
        multiplying = True

    elif event == '/':
        x = int(textBox.get())
        clearValue(textBox)
        dividing = True
    
    elif event == '=':
        if adding:
            y = int(textBox.get())
            textBox.update(value=str(x+y))
            adding = False
        elif subtracting:
            y = int(textBox.get())
            textBox.update(value=str(x-y))
            subtracting = False
        elif multiplying:
            y = int(textBox.get())
            textBox.update(value=str(x*y))
            multiplying = False
        elif dividing:
            y = int(textBox.get())
            if not y == 0:
                textBox.update(value=str(x/y)[:-2])
            else: textBox.update('DIV BY 0')
            dividing = False


window.close()