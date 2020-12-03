import PySimpleGUI as sg

sg.theme('Default1')

layout = [
    [sg.Input(size=(29 ,0), font=('Helvetica', 11), key='display'), sg.Button('⌫', size=(3,1), font=('Helvetica', 10)), sg.Button('CE', size=(3,1))],
    [sg.Button('7', size=(8,2)), sg.Button('8', size=(8,2)), sg.Button('9', size=(8,2)), sg.Button('/', size=(8,2), button_color=('black', 'orange'))],
    [sg.Button('4', size=(8,2)), sg.Button('5', size=(8,2)), sg.Button('6', size=(8,2)), sg.Button('*', size=(8,2), button_color=('black', 'orange'))],
    [sg.Button('1', size=(8,2)), sg.Button('2', size=(8,2)), sg.Button('3', size=(8,2)), sg.Button('+', size=(8,2), button_color=('black', 'orange'))],
    [sg.Button(',', size=(8,2)), sg.Button('0', size=(8,2)), sg.Button('=', size=(8,2), button_color=('black', 'orange')), sg.Button('-', size=(8,2), button_color=('black', 'orange'))],
    [sg.Multiline(size=(37, 9), font=('Helvetica', 11), disabled=True, key=('history'))],
    [sg.Button('Limpar histórico')]
]

window = sg.Window('Calculadora', layout)

display = []
history = False
historico = []

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event in '0123456789,+-/*':
        display.append(event.replace(',', '.'))
        window.Element('display').Update(''.join(display))
        #window['display'].Update(''.join(display))
    if event == '=':

        if len(display) == 0:
            continue
        
        result = ''.join(display)
        historico.append('{} = {}\n'.format(result, eval(result)))
        result = str(eval(result))
        display.clear()
        display.append(result)

        window.Element('display').Update(display)
        
        texto = ''
        for i in range(len(historico)):
            texto = texto+historico[i]

        window.Element('history').Update(texto)
    if event == 'CE':
        display.clear()
        window.Element('display').Update('')
    if event == '⌫':
        if len(display) == 0:
            continue
        
        display.pop()
        window.Element('display').Update(''.join(display))
    if event == 'Limpar histórico':
        historico.clear()
        window.Element('history').Update('')

window.close()