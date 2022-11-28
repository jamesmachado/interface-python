import PySimpleGUI as sg

class Tela:
    def __init__(self):

        layout = [
            [sg.Text('nome:', size=(5,0)), sg.Input(size=(60,0),key='nome')],

            [sg.Text('telefone:',size=(5,0)), sg.Input(size=(60,0),key='telefone')],

            [sg.Text('Quais provedores de email sao aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'), sg.Checkbox('Outlook',key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Button('salvar')]
        ] 

        self.janela = sg.Window('dados do usuario').layout(layout)

        

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
           
            telefone = self.values['telefone']

            aceita_Gmail = self.values['Gmail']
            aceita_Outlook = self.values['Outlook']
            aceita_Yahoo = self.values['Yahoo']
            print(f'nome: {nome}')
           
           
            print(f'telefone: {telefone}')
            
            print(f'aceita Gmail: {aceita_Gmail}')
            print(f'aceita Otlook: {aceita_Outlook}')
            print(f'aceita Yahoo: {aceita_Yahoo}')
        

tela = Tela()
tela.Iniciar()