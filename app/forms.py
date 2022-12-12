from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired



class DadosUsuario(FlaskForm):
    genero = RadioField( 'genero', choices=['Masculino', 'Feminino'], validators=[DataRequired()])
    comunicacao = RadioField( 'comunicacao', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    repetitivos = RadioField( 'repetitivos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    social = RadioField( 'social', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    fala = RadioField( 'fala', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    olhos = RadioField( 'olhos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    risos = RadioField( 'risos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    carinho = RadioField( 'carinho', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    relacionamento = RadioField( 'relacionamento', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    brinquedos = RadioField( 'brinquedos', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    nao_verbal = RadioField( 'nao_verbal', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    monotona = RadioField( 'monotona', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    pergunta = RadioField( 'pergunta', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    expressao = RadioField( 'expressao', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    perigo = RadioField( 'perigo', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    tempo = RadioField( 'tempo', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    balanca = RadioField( 'balanca', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    rotina = RadioField( 'rotina', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    agitado = RadioField( 'agitado', choices=['Sempre', 'Quase Sempre', 'Raramente', 'Nunca'], validators=[DataRequired()])
    
    

    submit = SubmitField('Enviar')

