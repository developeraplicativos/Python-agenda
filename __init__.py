from flask import Flask, jsonify, make_response, redirect, url_for, render_template
from datetime import datetime
from agenda_file import Agenda

app = Flask(__name__)

@app.route('/')
def home():
    return "BEM VINDO q"

@app.route('/desenvolvedor')
def desenvolvedor():
    return render_template( "emerson.html")

@app.route('/acesso', methods=['POST'])
def home2():
    return jsonify({'access':True, 'error': False})

@app.route('/visualizar', methods=['GET'])
def home3():
    lista_atividade = [
        {'ordem':1,'nome':'correr'},
        {'ordem':2,'nome':'ler'},
        {'ordem':3,'nome':'tomar remédio'},
        {'ordem':4,'nome':'trabalhar'} 
    ]
    agenda = Agenda()
    lista_atividades = agenda.visualizar_linhas()
    print([lista_atividades] )
    # print(lista_atividades,'< nova')
    # return jsonify({'visualizar': None,'error':False})
    # return jsonify({'visualizar': agenda,'error':False})
    return render_template('visualizar_agenda.html', agenda=lista_atividades, data=datetime.now() )

@app.route('/editar', methods=['POST'])
def home4(): 
    return jsonify({'update':True, 'error': False})


@app.route('/buscar', methods=['POST'])
def home5():
    return jsonify({'search': 'Emerson Rodrigues', 'error': False})

@app.route('/excluir', methods=['POST'])
def home6():
    return jsonify({'delete': True})

@app.route('/adicionar', methods=['POST'])
def home7():
    return jsonify({'add': True})
 

if __name__ == "__main__":
    app.run(debug=True)