from flask import Flask, render_template, request, redirect, url_for, flash 

app = Flask(__name__)
 
@app.route()
def visualizar():  
    return {}  

def editar(): 
    return {}

def buscar():
    return {}

def excluir():
    return {}

def reordenar(atividades): 
    return {}

def adicionar():
    return {}
    
if __name__ == "__name__":
    app.run(debug=True)
