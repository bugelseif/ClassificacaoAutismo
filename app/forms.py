from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired



class DadosUsuario(FlaskForm):
    genero = RadioField( 'genero', choices=['Masculino', 'Feminino'])
    comunicacao = RadioField( 'comunicacao', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    repetitivos = RadioField( 'repetitivos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    social = RadioField( 'social', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    fala = RadioField( 'fala', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    olhos = RadioField( 'olhos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    risos = RadioField( 'risos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    carinho = RadioField( 'carinho', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    relacionamento = RadioField( 'relacionamento', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    brinquedos = RadioField( 'brinquedos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    nao_verbal = RadioField( 'nao_verbal', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    monotona = RadioField( 'monotona', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    pergunta = RadioField( 'pergunta', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    expressao = RadioField( 'expressao', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    perigo = RadioField( 'perigo', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    tempo = RadioField( 'tempo', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    balanca = RadioField( 'balanca', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    rotina = RadioField( 'rotina', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    agitado = RadioField( 'agitado', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'])
    
    
    
    submit = SubmitField('Sign In')

