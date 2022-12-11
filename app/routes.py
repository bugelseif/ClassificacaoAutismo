import json
from flask import jsonify, render_template, flash, request
from app.forms import DadosUsuario
from .process.arvore import teste
from app import app
import requests




@app.route('/')
@app.route('/index')
def index():                
    return render_template('base.html')

@app.route('/exemplo') # rota apenas de exemplo
def exemplo(): 
    dados = "1,0,1,3,3,2,0,1,1,0,0,1,0,0,1,0,0,0,1"
    response = requests.get("http://127.0.0.1:5000/resultado/" + dados)
    resposta = response.json()
    return jsonify(resposta)

@app.route('/resultado/<dados>')# recebe dados anexados na rota, no momento recebe uma string e separa elementos por vírgula, formatação pode ser modificada depois
def resultado(dados): 
    #dados = dados.split(",")
    verificacao = teste(dados) 
    return jsonify(verificacao)

# Exemplo utilizando formatação do form, eu usei letras do alfabeto como argumentos mas no form seriam o name de cada campo 
@app.route('/exemploForms')
def exemplo_form(): 
    dados = "a=1&b=0&c=1&d=3&e=3&f=2&g=0&h=1&i=1&j=0&k=0&l=1&m=0&n=0&o=1&p=0&q=0&r=0&s=1"   
    response = requests.get("http://127.0.0.1:5000/resultadoForms?" + dados)
    resposta = response.json()
    return jsonify(resposta)


# É para funcionar com form, a orderm dos dados precisa ser a mesma que do arquivo csv usado para criar a árvore
@app.route('/resultadoForms')
def resultado_form(): 
    info = request.args.values()
    dados = "".join(info)
    verificacao = teste(dados) 
    return jsonify(verificacao)

@app.route('/usuario')
def usuario(): 
    form = DadosUsuario()
    if form.validate_on_submit():#verifica se tem informaçoes no formulario
        teste = form.genero.data
        return render_template('classifica.html', teste=teste) # vai renderizar as informaçoes do html com o json 
    return render_template('classifica.html', form=form) #caso o form nao seja valido permanece na pagina escolha 

@app.route('/sobre')
def sobre(): 
        return render_template('sobre.html') # vai renderizar as informaçoes do html com o json 