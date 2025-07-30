from flask import Flask, jsonify, request, flash, make_response, redirect, url_for, render_template
from datetime import datetime
from Archives import Archives
from agenda_file import Agenda
from FormsAtividades import FormsAtividades


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345-kjslfdjkljd' # temporario - apenas para apresentação
'''wtforms secret keys contra csrf'''
#app.config['SECRET_KEY'] = 'SDFSDF_FDSFSDFFFDS'
#estudar flaskform

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
def visualizar(): 
    agenda = Agenda()
    lista_atividades = agenda.visualizar_linhas() 
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

@app.route('/adicionar', methods=['GET','POST']) 
def adicionar():
    form = FormsAtividades()
    # if request.method == 'GET': 
    #     return render_template('cadastro-atividade.html', form = form)
            
    if request.method == 'POST':
        try:
            if form.validate_on_submit():

                archive = Archives()  
                atividade = request.form.get('atividade')
                if archive.write_archive(atividade+'\n') :
                    flash("Nova atividade inserida com sucesso!", 'alert alert-success')
            
        except Exception as ex: 
            flash(f"Erro ao salvar atividade: {ex}", "alert alert-warning") 
            

    return render_template('cadastro-atividade.html', form=form )

        
    
    # return render_template('cadastro-atividade.html')

# @app.route('/sucesso')
# def sucesso():
#     return "Cadastrado com Sucesso"

# @app.route('/error')
# def error():
#     return "Erro durante o cadastro"

if __name__ == "__main__":
    app.run(debug=True)