import PySimpleGUI as sg

def returnDescription(imc):
	
	if(imc < 18.5):
		return 'Abaixo do peso'
	elif(imc >= 18.5 and imc <= 24.9):
		return 'Peso Normal'
	elif(imc >= 25 and imc <= 29.9):
		return 'Sobrepeso'
	elif(imc >= 30 and imc <= 34.9):
		return 'Obesidade Grau I'
	elif(imc >= 35 and imc <= 39.9):
		return 'Obesidade Grau II'
	elif(imc >= 40):
		return 'Obesidade Grau III ou Mórbida'

sg.theme('Default1')

layout = [

    [sg.Text('Calcular IMC', font=('Helvetica', 25))],
    [sg.Text('Peso '), sg.Input(key='peso', size=(10, 1))],
    [sg.Text('Altura'), sg.Input(key='altura', size=(10, 1))],
    [sg.Text('IMC'), sg.Input(default_text='', disabled=True, key='IMC')],
    [sg.Text('Resultado: ', size=(30,1), key='resultado')],
    [sg.Button('Calcular', size=(10,2)), sg.Button('Limpar', size=(10,2))],
    [sg.Text('Desenvolvido por Brenno Luan')]

]

window = sg.Window('Cálculo do IMC', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calcular' and values['peso'] and values['altura']:
        peso = float(values['peso'].replace(",", "."))
        altura = float(values['altura'].replace(",", "."))
        calculo = peso/(altura*altura)
        window.Element('resultado').Update(value='Resultado: {0}\n'.format(returnDescription(calculo)), visible=True)
        window.Element('IMC').Update(value=calculo)
    if event == 'Limpar':
        window.Element('peso').Update(value='')
        window.Element('altura').Update(value='')
        window.Element('IMC').Update(value='')
        window.Element('resultado').Update(value='Resultado: ')

window.close()